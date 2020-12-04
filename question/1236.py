import collections

urls = ["http://psn.wlyby.edu/wvoz", "http://psn.wlyby.edu/shez", "http://psn.wlyby.edu/upkr",
        "http://psn.wlyby.edu/ubmr", "http://psn.wlyby.edu/apgb", "http://psn.wlyby.edu/sbin",
        "http://psn.wlyby.edu/inmj", "http://cpq.jkvox.tech/mjkb", "http://lqr.shmtu.tech/rsvw",
        "http://ylk.fubmn.com/ypyh"]
edges = [[0, 8], [1, 6], [1, 7], [1, 4], [3, 3], [3, 4], [3, 7], [4, 1], [4, 0], [4, 3], [5, 5], [5, 8], [5, 5], [5, 0],
         [6, 8], [7, 2], [7, 7], [7, 4], [10, 7], [10, 4], [10, 3], [10, 4]]
startUrl = "http://psn.wlyby.edu/ubmr"


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        if not startUrl:
            return []

        q = collections.deque([startUrl])
        hostname = startUrl.split("/")[2]
        visited = {startUrl}

        while q:

            curr_url = q.popleft()

            for next_url in htmlParser.getUrls(curr_url):

                # "http://psn.wlyby.edu/upkr" has the same hostname but it is NOT part of links from
                # "http://psn.wlyby.edu/ubmr"
                if next_url not in visited and next_url.split("/")[2] == hostname:
                    q += [next_url]
                    visited.add(next_url)

        return list(visited)
