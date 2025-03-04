from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from game.world.managers.maps.MapManager import MapManager
from game.world.managers.objects.ai.CreatureAI import CreatureAI
from utils.constants.CustomCodes import Permits
from utils.constants.MiscCodes import ObjectTypeIds
from utils.constants.UnitCodes import CreatureReactStates, UnitStates, AIReactionStates, UnitFlags

if TYPE_CHECKING:
    from game.world.managers.objects.units.creature.CreatureManager import CreatureManager


class BasicCreatureAI(CreatureAI):
    def __init__(self, creature: Optional[CreatureManager]):
        super().__init__(creature)
        self.can_summon_guards = creature.can_summon_guards() if creature else False

    # override
    def update_ai(self, elapsed):
        super().update_ai(elapsed)
        if not self.creature or not self.creature.combat_target:
            return

        if self.has_spell_list():
            self.update_spell_list(elapsed)

        self.do_melee_attack_if_ready()

    # override
    def permissible(self, creature):
        return Permits.PERMIT_BASE_NORMAL

    # override
    def movement_inform(self, move_type=None, data=None, units=None):
        pass

    # override
    def move_in_line_of_sight(self, unit=None):
        if not self._is_ready_for_new_attack():
            return
        unit = self._get_proximity_target(unit=unit)
        if unit:
            self.creature.object_ai.attacked_by(unit)

    # override
    def just_respawned(self):
        self.can_summon_guards = self.creature.can_summon_guards() if self.creature else False
        super().just_respawned()

    # override
    def summoned_creatures_despawn(self, creature):
        self.can_summon_guards = self.creature.can_summon_guards() if self.creature else False

    def _is_ready_for_new_attack(self):
        return self.creature.is_alive and self.creature.is_spawned and len(self.creature.known_players) > 0 \
               and self._is_aggressive() and not self.creature.in_combat and not self.creature.is_evading \
               and not self.creature.unit_state & UnitStates.STUNNED \
               and not self.creature.unit_flags & UnitFlags.UNIT_FLAG_PACIFIED

    def _is_aggressive(self):
        return self.creature.react_state == CreatureReactStates.REACT_AGGRESSIVE

    def summon_guard(self, enemy):
        pass

    # TODO: Find proper place for this?
    def _get_proximity_target(self, unit=None):
        detection_range = self.creature.creature_template.detection_range
        source_units = list(self.creature.known_players.values()) if not unit else [unit]
        hostile_units = []
        for unit in source_units:
            if unit.beast_master:
                continue
            if not self.creature.is_hostile_to(unit):
                continue
            hostile_units.append(unit)
            active_pet = unit.pet_manager.get_active_controlled_pet()
            if active_pet:
                hostile_units.append(active_pet.creature)
        for victim in hostile_units:
            victim_distance = victim.location.distance(self.creature.location)
            if victim_distance > detection_range:
                continue
            # Sanctuary.
            if victim.unit_state & UnitStates.SANCTUARY:
                continue
            # Not while flying.
            if victim.unit_flags & UnitFlags.UNIT_FLAG_TAXI_FLIGHT:
                continue
            # Check for stealth/invisibility.
            can_detect_victim, alert = self.creature.can_detect_target(victim, victim_distance)
            if alert and victim.get_type_id() == ObjectTypeIds.ID_PLAYER and not victim.beast_master:
                self.send_ai_reaction(victim, AIReactionStates.AI_REACT_ALERT)
            if not can_detect_victim:
                continue
            # Basic LoS check.
            if not MapManager.los_check(victim.map_id, self.creature.get_ray_position(), victim.get_ray_position()):
                continue
            return victim
