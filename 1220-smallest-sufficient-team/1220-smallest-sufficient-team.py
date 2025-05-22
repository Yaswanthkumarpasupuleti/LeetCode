# class Solution:
#     result = []

#     def solve(self,people_skill,idx,temp,mask):
#         if idx == len(people):
#             if (mask == target_mask):
#                 if len(result) == 0 or len(result) >= len(temp):
#                     result = temp
#             return
        
#         if len(result) != 0 and len(temp) >= len(result):
#             return
#         #skip
#         solve(people_skill,idx+1,temp,mask)
        
#         #take
#         if (mask | people_skill[idx] != mask):
#             temp.append(idx)
#             solve(people_skill,idx+1,temp,(mask | people_skill[idx]))
#             temp.pop()

#     def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

#         n = len(req_skills)
#         m = len(people)
#         skills_map = {}
#         for i in range(n):
#             skillname = req_skills[i]
#             skills_map[skillname] = i
#         print(skills_map)
#         people_skill = []
#         for ele in people:
#             skill_bit = 0;
#             for ski in ele:
#                 skill_bit = skill_bit | (1 << skills_map[ski])
#             people_skill.append(skill_bit)  
#         target_mask = 2**n - 1
#         temp = []
#         self.solve(people_skill,0,temp,0) #starting mask= 0(0,0,0)
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        bit_skills = {}
        for i, skill in enumerate(req_skills): bit_skills[skill] = 1 << i
  
        target_skills = (1 << len(req_skills)) - 1
        dp = [None] * (target_skills + 1)
        dp[0] = []

        for i, person_skills in enumerate(people):
            person_bitmask = sum(bit_skills[skill] for skill in person_skills)
            for covered_skills, team in enumerate(dp):
                if team is None: continue
                new_skills = covered_skills | person_bitmask
                if new_skills == covered_skills: continue
                if dp[new_skills] is None or len(dp[new_skills]) > len(team) + 1 : dp[new_skills] = team + [i]

        return dp[target_skills]