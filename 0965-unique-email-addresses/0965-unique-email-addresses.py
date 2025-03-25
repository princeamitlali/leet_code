class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_list = []
        for email in emails:
            l_name,d_name = email.split('@')
            l_name = l_name.split('+')[0]
            l_name = l_name.replace('.','')
            email = l_name + '@' + d_name
            if email not in final_list:
                final_list.append(email)
        return len(final_list)
        