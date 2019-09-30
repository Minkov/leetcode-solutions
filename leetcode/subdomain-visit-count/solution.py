class Solution:
    def subdomainVisits(self, cpdomains):
        counts = dict()
        for cpdomain in cpdomains:
            [count, domain] = cpdomain.split(" ")
            count = int(count)
            parts = domain.split(".")
            parts.reverse()

            subdomains = []
            subdomains.append(parts[0])
            for part in parts[1:]:
                subdomains.append(part + "." + subdomains[-1])
            for subdomain in subdomains:
                if subdomain not in counts:
                    counts[subdomain] = 0
                counts[subdomain] += count


        result = []

        for domain, domain_count in counts.items():
            result.append('%d %s' % (domain_count, domain))

        return result


sol = Solution()
print(sol.subdomainVisits(["9001 discuss.leetcode.com"]))
print(sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
