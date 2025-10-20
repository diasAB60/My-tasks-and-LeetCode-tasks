coordinates = "h3"
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ( coordinates[0] == "a" or coordinates[0] == "c" or coordinates[0] == "e" or coordinates[0] == "g" ):
            if (int(coordinates[1]) % 2 != 0):
                return False
            elif (int(coordinates[1]) % 2 == 0):
                return True
        elif ( coordinates[0] == "b" or coordinates[0] == "d" or coordinates[0] == "f" or coordinates[0] == "h" ):
            if (int(coordinates[1]) % 2 != 0):
                return True
            elif (int(coordinates[1]) % 2 == 0):
                return False
print(Solution().squareIsWhite(coordinates))