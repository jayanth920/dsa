# def solve(nums):
#     reachmaxxing = 0
#     for i in range(len(nums)):
#         if i <= reachmaxxing:
#             reachmaxxing = max(reachmaxxing, i+nums[i])
#             if reachmaxxing >= len(nums)-1:
#                 return True
#     return False


# def solve(nums):
#     reachmaxxing = len(nums) - 1
#     for i in range(len(nums) - 2, -1, -1):
#         if i + nums[i] >= reachmaxxing:
#             reachmaxxing = min(reachmaxxing, i - nums[i])
#         if reachmaxxing <= 0:
#             return True
#     return False

# print(solve([2,3,1,1,4]))

# def findPlatform(arrival, departure):
#     n = len(arrival)

#     # Initialize the first departure as max_time
#     max_time = departure[0]
#     c = 1  # Platform counter

#     # Sort both arrays to ensure proper order of events
#     arrival.sort()
#     departure.sort()

#     # Iterate over the arrival array
#     for i in range(n - 1):
#         # If the next train arrives before the current train departs, we need another platform
#         if departure[i] > arrival[i + 1]:
#             c += 1
#         else:
#             # Update max_time if the next train arrives after the current max_time
#             if arrival[i + 1] > max_time:
#                 max_time = departure[i + 1]
#                 c -= 1

#     return c

# # Test case
# print(findPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))  # Output: 3
# print(findPlatform([900, 1100, 1235], [1000, 1200, 1240]))  # Output: 1
# print(findPlatform([200, 210, 300, 320, 350, 500], [230, 340, 320, 430, 400, 520]))  # Output: 2
# print(findPlatform([900, 940, 950, 1100, 1500, 1800], [920, 950, 1020, 1130, 1900, 2000]))  # Output: 3
# print(findPlatform([900, 940], [1000, 1200]))  # Output: 2
# print(findPlatform([800, 810, 820, 830, 840], [830, 840, 850, 860, 870]))  # Output: 5
# print(findPlatform([800, 830, 1000, 1030, 1200, 1500, 1600], [900, 1230, 1030, 1130, 1300, 1530, 1700]))  # Output: 3

# def solve(nums):
#     ptr = 0
#     i = 0
#     c = 0
#     while i < len(nums):
#         i = i + nums[i]
#         if i >= len(nums)-1:
#             return True
#         if nums[i] == 0:
#             return False

# print(solve([2,3,1,1,4]))
# print(solve([1, 2, 3, 4, 5]))
# print(solve([3, 2, 1, 0, 4]))

# def solve(haystack,needle):
#     if not needle:
#         return 0
#     if not haystack:
#         return -1

#     counter = 0
#     initial = -1
#     for i in range(len(haystack)):
#         if haystack[i] == needle[counter]:
#             if counter == 0:
#                 initial = i
#             counter += 1
#             if counter == len(needle):
#                 return initial
#         else:
#             if counter > 0:
#                 i = initial
#             counter = 0
#             initial = -1
#         i+=1
#     return -1

# hay = "leetcode"
# need = "leet"
# hay1 = "mississippi"
# need1 = "issip"
# # print(solve(hay, need))  # Output: 0
# print(solve(hay1, need1))  # Output: 4


# def solve(s):
#         ans = ""
#         res = []
#         for i in range(len(s)):
#             if s[i] != " ":
#                 ans+= s[i]
#                 if i+1 != len(s) and  s[i+1] == " ":
#                     print(i)
#                     res.append(ans)
#                     ans = ""
#                 elif i == len(s)-1:
#                     res.append(ans)
#         return res

# print(solve("   fly me   to   the moon  "))
# print(solve("Hello World"))


# def solve(nums1: list[str], nums2: list[str]) -> list[str]:
#     for i in range(len(nums1)):
#         nums1[i] = nums1[i].strip().lower().replace(" ", "")
#     for i in range(len(nums2)):
#         nums2[i] = nums2[i].strip().lower().replace(" ", "")
#     final = []
#     for i in range(len(nums2)):
#         if nums2[i] in nums1:
#             final.append(nums2[i])
#     print(final)
#     print(len(final))


# solve(
#     [
#         "Electron",
#         "webpack",
#         "stdlib",
#         "Neutralinojs",
#         "rocket.chat",
#         "JSON Schema",
#         "Nightwatch.js",
#         "AsyncAPI",
#         "GRAME",
#         "Joplin",
#         "cBioPortal for Cancer Genomics",
#         "Purr Data",
#         "Jenkins",
#         "AOSSIE",
#         "OpenRefine",
#         "Jitsi",
#         "Project Mesa",
#         "52°North Spatial Information Research GmbH",
#         "freifunk",
#         "Ceph",
#         "City of Boston",
#         "CircuitVerse.org",
#         "MIT App Inventor",
#         "Apertium",
#         "INCF",
#         "Open Chemistry",
#         "International Catrobat Association",
#         "Internet Archive",
#         "Learning Equality",
#         "Mixxx",
#         "Accord Project",
#         "OpenELIS Global",
#         "OpenStreetMap",
#         "Drupal Association",
#         "Wikimedia Foundation",
#         "Python Software Foundation",
#         "Plone Foundation",
#         "Uramaki LAB",
#         "PostgreSQL",
#         "MariaDB",
#         "Polypheny",
#         "Open Technologies Alliance - GFOSS",
#         "FOSSASIA",
#         "Creative Commons",
#         "R project for statistical computing",
#         "National Resource for Network Biology (NRNB)",
#         "Submitty",
#         "OpenWISP",
#         "Department of Biomedical Informatics, Emory University",
#         "The Honeynet Project",
#         "OWASP Foundation",
#         "OSGeo (Open Source Geospatial Foundation)",
#         "Data for the Common Good",
#         "Zendalona",
#         "OpenMRS",
#         "caMicroscope",
#         "IOOS",
#         "Internet Health Report",
#         "Chromium",
#         "DBpedia",
#         "AboutCode",
#         "Wagtail",
#         "openSUSE Project",
#         "Sugar Labs",
#         "BRL-CAD",
#         "LabLua",
#         "API Dash",
#         "Open HealthCare Network",
#         "omegaUp",
#         "Kubeflow",
#         "CVAT",
#         "Graphite",
#         "The Palisadoes Foundation",
#         "Zulip",
#         "Oppia Foundation",
#         "Git",
#         "The NetBSD Foundation",
#         "Haskell.org",
#         "JdeRobot",
#         "The ENIGMA Team",
#         "OpenCV",
#         "Rizin",
#         "FreeType",
#         "gprMax",
#         "The ns-3 Network Simulator Project",
#         "Software and Computational Systems Lab at LMU Munich",
#         "The JPF team",
#     ],
#     [
#         "rocket.chat",
#         "cBioPortal for Cancer Genomics",
#         "GRAME",
#         "Purr Data",
#         "XWiki",
#         "Processing Foundation",
#         "Jenkins",
#         "AOSSIE",
#         "52°North Spatial Information Research GmbH",
#         "AboutCode",
#         "Apertium",
#         "caMicroscope",
#         "Ceph",
#         "Chromium",
#         "CircuitVerse.org",
#         "Cockpit Project",
#         "Creative Commons",
#         "DBpedia",
#         "Department of Biomedical Informatics, Emory University",
#         "Drupal Association",
#         "freifunk",
#         "GitLab",
#         "INCF",
#         "International Catrobat Association",
#         "Internet Archive",
#         "Internet Health Report",
#         "Learning Equality",
#         "LibreHealth",
#         "MariaDB",
#         "Mathesar",
#         "Mayor's Office of New Urban Mechanics",
#         "MIT App Inventor",
#         "Mixxx",
#         "National Resource for Network Biology (NRNB)",
#         "Open Chemistry",
#         "Open Technologies Alliance - GFOSS",
#         "OpenMRS",
#         "OpenStreetMap",
#         "OpenWISP",
#         "OSGeo (Open Source Geospatial Foundation)",
#         "OWASP Foundation",
#         "Plone Foundation",
#         "PostgreSQL",
#         "Postman",
#         "Python Software Foundation",
#         "Qdrant",
#         "R project for statistical computing",
#         "Society for Arts and Technology (SAT)",
#         "Submitty",
#         "The Honeynet Project",
#         "Wagtail",
#         "Wikimedia Foundation",
#         "openSUSE Project",
#         "Sugar Labs",
#         "BRL-CAD",
#         "omegaUp",
#         "Oppia Foundation",
#         "The Palisadoes Foundation",
#         "Zulip",
#         "Git",
#         "The NetBSD Foundation",
#         "JdeRobot",
#         "The ENIGMA Team",
#         "OpenCV",
#         "Rizin",
#         "FreeType",
#         "gprMax",
#         "The ns-3 Network Simulator Project",
#         "Software and Computational Systems Lab at LMU Munich",
#         "The JPF team",
#     ],
# )




# Random Number Guessing Game --------------------------------------


# import random

# top = input("ENTER A DIGIT !!\n")
# if top.isdigit():
#     top = int(top)
#     if top <= 0:
#         print("PLEASE ENTER A VALID NUMBER NEXT TIME !\n")
# else:
#     print("ENTER A VALID NUMBER NEXT TIME !!\n")

# ans = random.randint(1,top)

# answered = False

# while answered == False:
#     guess = input("GUESS A NUMBER !!\n")
#     if guess.isdigit():
#         guess = int(guess)
#         if guess <= 0:
#             print("PLEASE ENTER A VALID NUMBER NEXT TIME !\n")
#     if guess == ans:
#         print("YOU GUESSED IT CONGRATS !!!!!!!!!!!!!!!!!!!")
#         answered = True
#     elif guess > ans:
#         print("AAH GO LOWER...")
#     elif guess < ans:
#         print("AAH GO MORE...")
#     else:
#         print("YOU GOT IT WRONG MY BRO.....TRY AGAIN !!\n")
        
# import random

# # Outcomes
# outcomes = ["rock", "paper", "scissors"]

# # Initial scores
# cscore = 0
# pscore = 0

# while True:
#     player = input("Type Rock/Paper/Scissors to play or press Q to quit!\n").lower()
    
#     if player == "q":
#         break
#     if player not in outcomes:
#         print("Invalid input, please try again.")
#         continue
    
#     comp = random.choice(outcomes)
#     print(f"Computer chose {comp}")

#     if comp == player:
#         print("TIE")
#     elif (comp == "rock" and player == "scissors") or \
#          (comp == "scissors" and player == "paper") or \
#          (comp == "paper" and player == "rock"):
#         print(f"Computer Wins! {comp} beats {player}")
#         cscore += 1
#     else:
#         print(f"Player Wins! {player} beats {comp}")
#         pscore += 1

#     print(f"Player Score: {pscore}, Computer's Score: {cscore}")

# print("Thanks for playing!")