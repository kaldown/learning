class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = numRows
        result = []
        count = 0
        while count < len(s):
            # decrease amount until it reaches 1 letter
            # then start all over again from the highest shift
            if i == numRows:
                # mark all
                result.append([index for index in range(count, count+numRows)])
                count += numRows
            else:
                # put 0 on everything except the number
                row = [-1 for _ in range(numRows)]
                row[i-1] = count
                result.append(row)
                count += 1
            i -= 1
            if i <= 1:
                i = numRows
        # fill the matrix
        for row in result:
            for i, num in enumerate(row):
                if num < len(s) and num != -1:
                    row[i] = s[num]

        r = ''
        for i in range(numRows):
            for row in result:
                r += row[i] if str(row[i]).isalpha() or row[i] in [',', '.'] else ''
        return r

