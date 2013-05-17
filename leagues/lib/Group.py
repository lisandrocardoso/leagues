# -*- coding: utf-8 -*-


from BaseStage import BaseStage

import Tools


class Group(BaseStage):

    def generate_fixtures(self):
        if not self.teams:
            return None

        def shift_right(input_list):
            working_list = input_list
            first = working_list[0]
            working_list.remove(first)
            carry = working_list[0]
            working_list.remove(carry)
            working_list.append(carry)
            working_list.insert(0, first)
            return working_list

        def reverse(input_list):
            return input_list[::-1]

        a_list = []

        for item in self.teams:
            a_list.append(item)

        b_list = reverse(a_list)

        for it in range(0, len(self.teams) - 1): 
            self.fixture_lists.append([])
            for idx in range(0, len(self.teams) / 2): 
                self.fixture_lists[it].append([a_list[idx], b_list[idx]])
            a_list = shift_right(a_list)
            b_list = reverse(a_list)

        if self.legs == 2:
            cur_list = self.fixture_lists
            for f in cur_list:
                new_f = []
                for m in f:
                    reverse_m = [ m[1], m[0] ]
                    new_f.append(reverse_m)
                self.fixture_lists.append(new_f)

        return self.fixture_lists
