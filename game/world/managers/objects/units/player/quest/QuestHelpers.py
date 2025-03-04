from utils.constants.MiscCodes import QuestSpecialFlags, QuestMethod


class QuestHelpers:

    @staticmethod
    def is_instant_complete_quest(quest_template):
        return quest_template.Method == QuestMethod.QUEST_AUTOCOMPLETE

    @staticmethod
    def is_instant_with_no_requirements(quest_template):
        return QuestHelpers.is_instant_complete_quest(quest_template) and \
               not QuestHelpers.requires_items_or_gos(quest_template)

    @staticmethod
    def is_quest_repeatable(quest_template):
        return quest_template.SpecialFlags & QuestSpecialFlags.QUEST_SPECIAL_FLAG_REPEATABLE

    @staticmethod
    def is_quest_scripted(quest_template):
        return quest_template.SpecialFlags & QuestSpecialFlags.QUEST_SPECIAL_FLAG_SCRIPT

    @staticmethod
    # noinspection PyUnusedLocal
    def has_required_items_for_quest(player_mgr, quest_template):
        for index in range(1, 5):
            req_item = eval(f'quest_template.ReqItemId{index}')
            req_item_count = eval(f'quest_template.ReqItemCount{index}')
            if req_item and not player_mgr.inventory.get_item_count(req_item) >= req_item_count:
                return False
        return True

    @staticmethod
    # noinspection PyUnusedLocal
    def has_item_reward(quest_template):
        for index in range(1, 5):
            if eval(f'quest_template.RewItemId{index}') > 0:
                return True
        return False

    @staticmethod
    # noinspection PyUnusedLocal
    def requires_items_or_gos(quest_template):
        for index in range(1, 5):
            if eval(f'quest_template.ReqItemId{index}') > 0:
                return True
            if eval(f'quest_template.ReqCreatureOrGOId{index}') > 0:
                return True
        return False

    @staticmethod
    # noinspection PyUnusedLocal
    def has_pick_reward(quest_template):
        for index in range(1, 5):
            if eval(f'quest_template.RewChoiceItemId{index}') > 0:
                return True
        return False

    @staticmethod
    def generate_rew_choice_item_list(quest_template):
        return [quest_template.RewChoiceItemId1, quest_template.RewChoiceItemId2, quest_template.RewChoiceItemId3, quest_template.RewChoiceItemId4,
                quest_template.RewChoiceItemId5, quest_template.RewChoiceItemId6]

    @staticmethod
    def generate_rew_choice_count_list(quest_template):
        return [quest_template.RewChoiceItemCount1, quest_template.RewChoiceItemCount2, quest_template.RewChoiceItemCount3,
                quest_template.RewChoiceItemCount4, quest_template.RewChoiceItemCount5, quest_template.RewChoiceItemCount6]

    @staticmethod
    def generate_rew_item_list(quest_template):
        return [quest_template.RewItemId1, quest_template.RewItemId3, quest_template.RewItemId2, quest_template.RewItemId4]

    @staticmethod
    def generate_rew_count_list(quest_template):
        return [quest_template.RewItemCount1, quest_template.RewItemCount2, quest_template.RewItemCount3, quest_template.RewItemCount4]

    @staticmethod
    def generate_req_item_list(quest_template):
        return [quest_template.ReqItemId1, quest_template.ReqItemId2, quest_template.ReqItemId3, quest_template.ReqItemId4]

    @staticmethod
    def generate_req_item_count_list(quest_template):
        return [quest_template.ReqItemCount1, quest_template.ReqItemCount2, quest_template.ReqItemCount3, quest_template.ReqItemCount4]

    @staticmethod
    def has_item_requirements(quest_template):
        return quest_template.ReqItemCount1 + quest_template.ReqItemCount2 + quest_template.ReqItemCount3 + quest_template.ReqItemCount4 > 0

    @staticmethod
    def generate_req_source_list(quest_template):
        return [quest_template.ReqSourceId1, quest_template.ReqSourceId2, quest_template.ReqSourceId3, quest_template.ReqSourceId4]

    @staticmethod
    def generate_req_source_count_list(quest_template):
        return [quest_template.ReqSourceCount1, quest_template.ReqSourceCount2, quest_template.ReqSourceCount3, quest_template.ReqSourceCount4]

    @staticmethod
    def generate_req_creature_or_go_list(quest_template):
        return [quest_template.ReqCreatureOrGOId1, quest_template.ReqCreatureOrGOId2, quest_template.ReqCreatureOrGOId3, quest_template.ReqCreatureOrGOId4]

    @staticmethod
    def generate_req_creature_or_go_count_list(quest_template):
        return [quest_template.ReqCreatureOrGOCount1, quest_template.ReqCreatureOrGOCount2, quest_template.ReqCreatureOrGOCount3,
                quest_template.ReqCreatureOrGOCount4]

    @staticmethod
    def generate_req_spell_cast_list(quest_template):
        return [quest_template.ReqSpellCast1, quest_template.ReqSpellCast2, quest_template.ReqSpellCast3, quest_template.ReqSpellCast4]

    @staticmethod
    def generate_objective_text_list(quest_template):
        return [quest_template.ObjectiveText1, quest_template.ObjectiveText2, quest_template.ObjectiveText3, quest_template.ObjectiveText4]

    @staticmethod
    def generate_rew_faction_reputation_list(quest_template):
        return [quest_template.RewRepFaction1, quest_template.RewRepFaction2, quest_template.RewRepFaction3,
                quest_template.RewRepFaction4, quest_template.RewRepFaction5]

    @staticmethod
    def generate_rew_faction_reputation_gain_list(quest_template):
        return [quest_template.RewRepValue1, quest_template.RewRepValue2, quest_template.RewRepValue3,
                quest_template.RewRepValue4, quest_template.RewRepValue5]
