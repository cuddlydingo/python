import ex26

from pprint import pprint

print(f"I am currently {ex26.height} inches tall.")

ex26.__dict__["height"] = 1000
print(f"I am now {ex26.height} inches tall.")

ex26.height = 12
print(f"oops, now I'm {ex26.__dict__['height']} inches tall.")


print(pprint.__doc__)
help(pprint)
