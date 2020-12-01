mora = [20000, 40000, 60000, 80000, 100000, 120000]
elemental_materials = [1, 3, 6, 3, 6, 6]
lightning_prism = [2, 4, 8, 12, 20]
cor_lapis = [3, 10, 20, 30, 45, 60]
nectar = [3, 15, 12, 18, 12, 24]

level = int(input("type your ascension level:"))

if level >= 7:
    print(f"Ascension level {level} is not in the game. Please type again.")
else:
    mora1 = int(input("How much Mora do you have:"))
    cor_lapis1 = int(input("How many Cor Lapis do you have:"))

if level == 1:
    elemental_mat = int(input("How many Vajrada Amethyst Sliver do you have:"))
    nectar1 = int(input("How many Whopperflower Nectar do you have:"))

    if mora1 >= mora[0]:
        print("\n[You have gathered enough mora for the current ascension.")
        result = mora1 - mora[0]
        if result > 0:
            print(f"You have an excess of {result} mora.")
        require = 40000
        print(f"You require {require} for ascension 2.]\n")
    else:
        require = mora[0] - mora1
        print(f"\nYou require {require} more of mora.")

    if elemental_mat >= elemental_materials[0]:
        print("\n[You have gathered enough electro sliver for " +
              "the current ascension.")
        result = elemental_mat - elemental_materials[0]
        if result > 0:
            print(f"You have an excess of {result} electro sliver.")
        require = [9, 3]
        print(f"You require {require[0]} of slivers or {require[1]} of " +
              "fragments for ascension 2.]\n")
    else:
        require = elemental_materials[0] - elemental_mat
        print(f"\nYou require {require} more of electro sliver.")

    if cor_lapis1 >= cor_lapis[0]:
        print("[You have gathered enough cor lapis for " +
              "the current ascension.")
        result = cor_lapis1 - cor_lapis[0]
        if result > 0:
            print(f"You have an excess of {result} cor lapis.")
        require = 10
        print(f"You require {require} for ascension 2.]\n")
    else:
        require = cor_lapis[0] - cor_lapis1
        print(f"\nYou require {require} more of cor lapis.")

    if nectar1 >= nectar[0]:
        print("\n[You have gathered enough whopperflower nectar for " +
              "the current ascension.")
        result = nectar1 - nectar[0]
        if result > 0:
            print(f"You have an excess of {result} whopperflower nectar.")
        require = 15
        print(f"You require {require} for ascension 2.]\n")
    else:
        require = nectar[0] - nectar1
        print(f"\nYou require {require} more of whopperflower nectar.")

    result = mora1 + elemental_mat + cor_lapis1 + nectar1
    if result >= cor_lapis[0] + nectar[0] + mora[0] + elemental_materials[0]:
        print(f"\nYou have gathered all necessary materials for ascending.")

if level == 2:
    elemental_mat = int(
        input("How many Vajrada Amethyst Fragments do you have:"))
    lightning_prism1 = int(input("How many Lightning Prism do you have:"))
    nectar1 = int(input("How many Whopperflower Nectar do you have:"))

    if mora1 >= mora[1]:
        print("\n[You have gathered enough mora for the current ascension.")
        result = mora1 - mora[1]
        if result > 0:
            print(f"You have an excess of {result} mora.")
        require = 60000
        print(f"You require {require} for ascension 3.]\n")
    else:
        require = mora[1] - mora1
        print(f"\nYou require {require} more of mora.")

    if lightning_prism1 >= lightning_prism[0]:
        print("\n[You have gathered enough lightning prism for " +
              "the current ascension.")
        result = lightning_prism1 - lightning_prism[0]
        if result > 0:
            print(f"You have an excess of {result} lightning prism.")
        require = 4
        print(f"You require {require} for ascension 3.]\n")
    else:
        require = lightning_prism[0] - lightning_prism1
        print(f"\nYou require {require} more of lightning prism.")

    if elemental_mat >= elemental_materials[1]:
        print("\n[You have gathered enough electro fragments for " +
              "the current ascension.")
        result = elemental_mat - elemental_materials[1]
        if result > 0:
            print(f"You have an excess of {result} electro fragments.")
        require = [18, 6]
        print(f"You require {require[0]} of slivers or {require[1]} of " +
              "fragments for ascension 3.]\n")
    else:
        require = elemental_materials[1] - elemental_mat
        print(f"\nYou require {require} more of electro fragments.")

    if cor_lapis1 >= cor_lapis[1]:
        print("[You have gathered enough cor lapis for " +
              "the current ascension.")
        result = cor_lapis1 - cor_lapis[1]
        if result > 0:
            print(f"You have an excess of {result} cor lapis.")
        require = 20
        print(f"You require {require} for ascension 3.]\n")
    else:
        require = cor_lapis[1] - cor_lapis1
        print(f"\nYou require {require} more of cor lapis.")

    if nectar1 >= nectar[1]:
        print("\n[You have gathered enough whopperflower nectar for " +
              "the current ascension.")
        result = nectar1 - nectar[1]
        if result > 0:
            print(f"You have an excess of {result} whopperflower nectar.")
        require = [36, 12]
        print(f"You require {require[0]} of whopperflower nectars or " +
              f"{require[1]} of shimmering nectars ascension 3.]\n")
    else:
        require = nectar[1] - nectar1
        print(f"\nYou require {require} more of whopperflower nectar.")

    result = lightning_prism1 + mora1 + elemental_mat + cor_lapis1 + nectar1
    if result >= lightning_prism[0] + cor_lapis[1] + nectar[1] + mora[1] + elemental_materials[1]:
        print(f"\nYou have gathered all necessary materials for ascending.")

if level == 3:
    elemental_mat = int(
        input("How many Vajrada Amethyst Fragments do you have:"))
    lightning_prism1 = int(input("How many Lightning Prism do you have:"))
    nectar1 = int(input("How many Shimmering Nectar do you have:"))

    if mora1 >= mora[2]:
        print("\n[You have gathered enough mora for the current ascension.")
        result = mora1 - mora[2]
        if result > 0:
            print(f"You have an excess of {result} mora.")
        require = 80000
        print(f"You require {require} for ascension 4.]\n")
    else:
        require = mora[2] - mora1
        print(f"\nYou require {require} more of mora.")

    if lightning_prism1 >= lightning_prism[1]:
        print("\n[You have gathered enough lightning prism for " +
              "the current ascension.")
        result = lightning_prism1 - lightning_prism[1]
        if result > 0:
            print(f"You have an excess of {result} lightning prism.")
        require = 8
        print(f"You require {require} for ascension 4.]\n")
    else:
        require = lightning_prism[1] - lightning_prism1
        print(f"\nYou require {require} more of lightning prism.")

    if elemental_mat >= elemental_materials[2]:
        print("\n[You have gathered enough electro fragments for " +
              "the current ascension.")
        result = elemental_mat - elemental_materials[2]
        if result > 0:
            print(f"You have an excess of {result} electro fragments.")
        require = [27, 9, 3]
        print(f"You require {require[0]} of slivers or {require[1]} of " +
              f"fragments or {require[2]} of chunks for ascension 3.]\n")
    else:
        require = elemental_materials[2] - elemental_mat
        print(f"\nYou require {require} more of electro fragments.")

    if cor_lapis1 >= cor_lapis[2]:
        print("[You have gathered enough cor lapis for " +
              "the current ascension.")
        result = cor_lapis1 - cor_lapis[2]
        if result > 0:
            print(f"You have an excess of {result} cor lapis.")
        require = 30
        print(f"You require {require} for ascension 4.]\n")
    else:
        require = cor_lapis[2] - cor_lapis1
        print(f"\nYou require {require} more of cor lapis.")

    if nectar1 >= nectar[2]:
        print("\n[You have gathered enough whopperflower nectar for " +
              "the current ascension.")
        result = nectar1 - nectar[2]
        if result > 0:
            print(f"You have an excess of {result} whopperflower nectar.")
        require = [54, 18]
        print(f"You require {require[0]} of whopperflower nectars or " +
              f"{require[1]} of shimmering nectars ascension 4.]\n")
    else:
        require = nectar[2] - nectar1
        print(f"\nYou require {require} more of whopperflower nectar.")

    result = lightning_prism1 + mora1 + elemental_mat + cor_lapis1 + nectar1
    if result >= lightning_prism[1] + cor_lapis[2] + nectar[2] + mora[2] + elemental_materials[2]:
        print(f"\nYou have gathered all necessary materials for ascending.")

if level == 4:
    elemental_mat = int(input("How many Vajrada Amethyst Chunks do you have:"))
    lightning_prism1 = int(input("How many Lightning Prism do you have:"))
    nectar1 = int(input("How many Shimmering Nectar do you have:"))

    if mora1 >= mora[3]:
        print("\n[You have gathered enough mora for the current ascension.")
        result = mora1 - mora[3]
        if result > 0:
            print(f"You have an excess of {result} mora.")
        require = 100000
        print(f"You require {require} for ascension 5.]\n")
    else:
        require = mora[3] - mora1
        print(f"\nYou require {require} more of mora.")

    if lightning_prism1 >= lightning_prism[2]:
        print("\n[You have gathered enough lightning prism for " +
              "the current ascension.")
        result = lightning_prism1 - lightning_prism[2]
        if result > 0:
            print(f"You have an excess of {result} lightning prism.")
        require = 12
        print(f"You require {require} for ascension 5.]\n")
    else:
        require = lightning_prism[2] - lightning_prism1
        print(f"\nYou require {require} more of lightning prism.")

    if elemental_mat >= elemental_materials[3]:
        print("\n[You have gathered enough electro chunks for " +
              "the current ascension.")
        result = elemental_mat - elemental_materials[3]
        if result > 0:
            print(f"You have an excess of {result} electro chunks.")
        require = [54, 18, 6]
        print(f"You require {require[0]} of slivers or {require[1]} of " +
              f"fragments or {require[2]} of chunks for ascension 3.]\n")
    else:
        require = elemental_materials[3] - elemental_mat
        print(f"\nYou require {require} more of electro chunks.")

    if cor_lapis1 >= cor_lapis[3]:
        print("[You have gathered enough cor lapis for " +
              "the current ascension.")
        result = cor_lapis1 - cor_lapis[3]
        if result > 0:
            print(f"You have an excess of {result} cor lapis.")
        require = 45
        print(f"You require {require} for ascension 5.]\n")
    else:
        require = cor_lapis[3] - cor_lapis1
        print(f"\nYou require {require} more of cor lapis.")

    if nectar1 >= nectar[3]:
        print("\n[You have gathered enough whopperflower nectar for " +
              "the current ascension.")
        result = nectar1 - nectar[3]
        if result > 0:
            print(f"You have an excess of {result} whopperflower nectar.")
        require = [108, 36, 12]
        print(f"You require {require[0]} of whopperflower nectars or " +
              f"{require[1]} of shimmering nectars " +
              f"{require[2]} of energy nectars for ascension 5.]\n")
    else:
        require = nectar[3] - nectar1
        print(f"\nYou require {require} more of whopperflower nectar.")

    result = lightning_prism1 + mora1 + elemental_mat + cor_lapis1 + nectar1
    if result >= lightning_prism[2] + cor_lapis[3] + nectar[3] + mora[3] + elemental_materials[3]:
        print(f"\nYou have gathered all necessary materials for ascending.")


if level == 5:
    elemental_mat = int(input("How many Vajrada Amethyst Chunks do you have:"))
    lightning_prism1 = int(input("How many Lightning Prism do you have:"))
    nectar1 = int(input("How many Energy Nectar do you have:"))

    if mora1 >= mora[4]:
        print("\n[You have gathered enough mora for the current ascension.")
        result = mora1 - mora[4]
        if result > 0:
            print(f"You have an excess of {result} mora.")
            require = 120000
            print(f"You require {require} for ascension 6.]\n")
    else:
        require = mora[4] - mora1
        print(f"\nYou require {require} more of mora.")

    if elemental_mat >= elemental_materials[4]:
        print("\n[You have gathered enough electro chunks for " +
              "the current ascension.")
        result = elemental_mat - elemental_materials[4]
        if result > 0:
            print(f"You have an excess of {result} electro chunks.")
            require = 6
            print(f"You require {require} for ascension 6.]\n")
    else:
        require = elemental_materials[4] - elemental_mat
        print(f"\nYou require {require} more of electro chunks.")

    if lightning_prism1 >= lightning_prism[3]:
        print("\n[You have gathered enough lightning prism for " +
              "the current ascension.")
        result = lightning_prism1 - lightning_prism[3]
        if result > 0:
            print(f"You have an excess of {result} lightning prism.")
        require = 20
        print(f"You require {require} for ascension 6.]\n")
    else:
        require = lightning_prism[3] - lightning_prism1
        print(f"\nYou require {require} more of lightning prism.")

    if cor_lapis1 >= cor_lapis[4]:
        print("[You have gathered enough cor lapis for " +
              "the current ascension.")
        result = cor_lapis1 - cor_lapis[4]
        if result > 0:
            print(f"You have an excess of {result} cor lapis.")
        require = 60
        print(f"You require {require} for ascension 6.]\n")
    else:
        require = cor_lapis[4] - cor_lapis1
        print(f"\nYou require {require} more of cor lapis.")

    if nectar1 >= nectar[4]:
        print("\n[You have gathered enough energy nectar for " +
              "the current ascension.")
        result = nectar1 - nectar[4]
        if result > 0:
            print(f"You have an excess of {result} energy nectar.")
        require = 24
        print(f"You require {require} for ascension 6.]\n")
    else:
        require = nectar[4] - nectar1
        print(f"\nYou require {require} more of energy nectar.")

    result = mora1 + elemental_mat + lightning_prism1 + cor_lapis1 + nectar1
    if result >= lightning_prism[3] + cor_lapis[4] + nectar[4] + mora[4] + elemental_materials[4]:
        print(f"\nYou have gathered all necessary materials for ascending.")

if level == 6:
    elemental_mat = int(input("How many Vajrada Amethyst Gemstone " +
                              "do you have:"))
    lightning_prism1 = int(input("How many Lightning Prism do you have:"))
    nectar1 = int(input("How many Energy Nectar do you have:"))

    if mora1 >= mora[5]:
        print("\n[You have gathered enough mora for the current ascension.")
        result = mora1 - mora[5]
        if result > 0:
            print(f"You have an excess of {result} mora.")
            require = []
            print(f"You require {require} for ascension 7.]\n")
    else:
        require = mora[5] - mora1
        print(f"\nYou require {require} more of mora.")

    if elemental_mat >= elemental_materials[5]:
        print("\n[You have gathered enough electro gemstones for " +
              " the current ascension.")
        result = elemental_mat - elemental_materials[5]
        if result > 0:
            print(f"You have an excess of {result} electro gemstones.")
            require = []
            print(f"You require {require} for ascension 7.]\n")
    else:
        require = elemental_materials[5] - elemental_mat
        print(f"\nYou require {require} more of electro gemstones.")

    if lightning_prism1 >= lightning_prism[4]:
        print("\n[You have gathered enough lightning prism for " +
              "the current ascension.")
        result = lightning_prism1 - lightning_prism[4]
        if result > 0:
            print(f"You have an excess of {result} lightning prism.")
        require = []
        print(f"You require {require} for ascension 7.]\n")
    else:
        require = lightning_prism[4] - lightning_prism1
        print(f"\nYou require {require} more of lightning prism.")

    if cor_lapis1 >= cor_lapis[5]:
        print("[You have gathered enough cor lapis for " +
              "the current ascension.")
        result = cor_lapis1 - cor_lapis[5]
        if result > 0:
            print(f"You have an excess of {result} cor lapis.")
        require = []
        print(f"You require {require} for ascension 7.]\n")
    else:
        require = cor_lapis[5] - cor_lapis1
        print(f"\nYou require {require} more of cor lapis.")

    if nectar1 >= nectar[5]:
        print("[You have gathered enough energy nectar for " +
              "the current ascension.")
        result = nectar1 - nectar[5]
        if result > 0:
            print(f"You have an excess of {result} energy nectar.")
        require = []
        print(f"You require {require} for ascension 7.]\n")
    else:
        require = nectar[5] - nectar1
        print(f"\nYou require {require} more of energy nectar")

    result = mora1 + elemental_mat + lightning_prism1 + cor_lapis1 + nectar1
    if result >= lightning_prism[4] + cor_lapis[5] + nectar[5] + mora[5] + elemental_materials[5]:
        print(f"\nYou have gathered all necessary materials for ascending.")
