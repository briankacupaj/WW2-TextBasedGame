import time
import random

items = []


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again.')


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print("")
    print_pause("Welcome to the world of the 1930s.")
    print_pause("You are serving as the leader of the new German state.")
    print_pause("Tensions are running high after your rise to power, and "
                "it is your job to rapidly expand, while trying not to upset "
                "any of the other global superpowers.")
    print_pause("The Allies want to maintain peace in Europe, and you have to"
                " try to use that to your advantage.")
    print_pause("You will be presented many decisions, and each thing you do "
                "will change the course of history.")
    print_pause("Good luck.")


def rhineland_intro():
    print("")
    print_pause("It is March of 1936. 17 years since the Treaty of "
                "Versailles. In this treaty we were forced to demilitarize "
                "the area known as the Rhineland. This region is home to all "
                "our Western Fronts.")
    print_pause("In order to reassert our military's power, we must first "
                "remilitarize this region.")
    print_pause("What shall we do?")
    rhineland()


def rhineland():
    rhineland_decision = valid_input('Send the troops into the region or '
                                     'push it off. (1|2) \n', ['1', '2'])
    if rhineland_decision == '1':
        items.append("Rhineland")
        print_pause("You picked to send in the military.")
        print_pause("The people rejuvenate! We are slowly undoing the unfair "
                    "treaty. The Allies back down after the lack of public "
                    "support for an invasion.")
    elif rhineland_decision == '2':
        print_pause("You picked to do nothing.")
        print_pause("This isn't worth our time right now.")
    else:
        rhineland()


def anschluss_intro():
    print("")
    print_pause("Now, we have the issue of Austria.")
    print_pause("Since the establishment of Austrian fascism in 1933, the "
                "Austrian people realize that they are in fact, Germans.")
    print_pause("We now have a choice. After the current Austrian Prime "
                "Minister has said he will not allow German unification, we "
                "must decide to let them get their way, or to force them "
                "into the Reich.")
    print_pause("What shall we do here?")
    anschluss_event()


def anschluss_event():
    anschluss_decision = valid_input('Invade the Austrians or ignore them? '
                                     '(1|2)\n', ['1', '2'])
    if anschluss_decision == '1':
        if "Rhineland" in items:
            print("")
            anschluss_success()
        if "Rhineland" not in items:
            index = random.randint(1, 6)
            if index < 3:
                anschluss_success()
            elif index > 3:
                anschluss_failure()
            elif index == 3:
                game_over_anschluss()
    elif anschluss_decision == '2':
        print_pause("We decide to ignore the Austrians.")
        print_pause("Their matters do not concern us at the moment.")
        sudetenland_intro()
    else:
        anschluss_event()


def anschluss_success():
    print("")
    print_pause("Our coup is a success!")
    print_pause("The NSDAP has taken power in Austria.")
    print_pause("The Wehrmacht enters to cheering crowds.")
    print_pause("The Allies turn their Heads.")
    items.append("Anschluss")
    sudetenland_intro()


def anschluss_failure():
    print("")
    print_pause("It is chaos in Vienna!")
    print_pause("Our coup has failed!")
    print_pause("The people have voted against unification and the Austrian "
                "government refuses to yield to our demands!")
    print_pause("We must look elsewhere...")
    sudetenland_intro()


def sudetenland_intro():
    print("")
    print_pause("It's 1938. Germans in Czechoslovakia are becoming more and "
                "more patriotic towards their homeland.")
    print_pause("These Germans are concentrated in the region known as the "
                "Sudetenland.")
    print_pause("Once part of German Austria, the Sudetenland was then "
                "shortly after seceded to Czechoslovakia.")
    print_pause("After the rise of fascism in Germany, these Germans feel "
                "now is the time to push for unification.")
    print_pause("We have the choice to host a conference between the Allied "
                "and Axis powers to discuss the future of this region.")
    print_pause("Or we can leave the Czechs to their own devices.")
    print_pause("What shall we do?")
    sudetenland_event()


def sudetenland_event():
    sudetenland_decision = valid_input('Host the Munich Conference or Forget '
                                       'about the Czechs. (1|2)\n',
                                       ['1', '2'])
    if sudetenland_decision == '1':
        if "Rhineland" and "Anschluss" in items:
            index2 = random.randint(1, 6)
            if index2 == 1:
                munich_diktat()
            else:
                munich_conference()

        elif "Anschluss" in items and "Rhineland" not in items:
            index2 = random.randint(1, 5)
            if index2 == 1:
                munich_diktat()
            elif index2 == 2:
                game_over_sudetenland()
            else:
                munich_conference()

        elif "Rhineland" in items and "Anschluss" not in items:
            index2 = random.randint(1, 4)
            if index2 == 1:
                game_over_sudetenland()
            elif index2 == 2:
                munich_diktat()
            else:
                munich_conference()

        elif "Rhineland" and "Anschluss" not in items:
            index2 = random.randint(1, 3)
            if index2 == 1:
                game_over_sudetenland()
            else:
                munich_diktat()

    elif sudetenland_decision == '2':
        if "Rhineland" and "Anschluss" not in items:
            print_pause("The Allies have found out about our plan to "
                        "consider invading the Czechs!")
            game_over_sudetenland()
        elif "Anschluss" in items and "Rhineland" not in items:
            index2 = random.randint(1, 5)
            if index2 == 1:
                print_pause("The Allies have found out about our plan to "
                            "consider invading the Czechs!")
                game_over_sudetenland()
            else:
                print_pause("We have decided to bypass the Czechs.")
                print_pause("Now we can either demand Danzig from Poland, "
                            "or turn our eyes to the West.")
                west_or_east()
        elif "Anschluss" not in items and "Rhineland" in items:
            index2 = random.randint(1, 5)
            if index2 == 1 or 2:
                print_pause("The Allies have found out about our plan to "
                            "consider invading the Czechs!")
                game_over_sudetenland()
            else:
                print_pause("We have decided to bypass the Czechs.")
                print_pause("Now we can either demand Danzig from Poland, or "
                            "turn our eyes to the West.")
                west_or_east()
        elif "Anschluss" and "Rhineland" in items:
            print_pause("We have decided to bypass the Czechs.")
            print_pause("Now we can either demand Danzig from Poland, or "
                        "turn our eyes to the West.")
            west_or_east()


def munich_conference():
    print("")
    print_pause("The Munich Conference is a success!")
    print_pause("The Sudetenland is ours.")
    print_pause("Per the agreement, we are not supposed to invade the rest "
                "of Czechoslovakia, but we choose to ignore that.")
    cze_invasion_success()


def munich_diktat():
    print("")
    print_pause("The Allies have denied us the Sudetenland!")
    print_pause("We now have the choice to either take it by force, or "
                "to back down.")
    print_pause("What shall we do?")
    diktat_choice()


def diktat_choice():
    diktat_decision = valid_input('Invade the Czechs or Back down (1|2)\n',
                                  ['1', '2'])
    if diktat_decision == '1':
        if "Rhineland" and "Anschluss" in items:
            index3 = random.randint(1, 6)
            if index3 == 1:
                game_over_sudetenland()
            else:
                print_pause("We declare war on Czechoslovakia, putting us at "
                            "war with the Allies.")
                items.append("War")
                cze_invasion_success()
        elif "Rhineland" in items and "Anschluss" not in items:
            index3 = random.randint(1, 6)
            if index3 == 1 or 2:
                game_over_sudetenland()
            else:
                print_pause("We declare war on Czechoslovakia, putting us at "
                            "war with the Allies.")
                items.append("War")
                cze_invasion_success()
        elif "Anschluss" in items and "Rhineland" not in items:
            index3 = random.randint(1, 5)
            if index3 == 1:
                game_over_sudetenland()
            else:
                print_pause("We declare war on Czechoslovakia, putting us at "
                            "war with the Allies.")
                items.append("War")
                cze_invasion_success()
        elif "Anschluss" and "Rhineland" not in items:
            game_over_sudetenland()

    elif diktat_decision == '2':
        print_pause("We have backed down.")
        if "Rhineland" and "Anschluss" not in items:
            game_over_sudetenland()
        elif "Anschluss" not in items and "Rhineland" in items:
            index3 = random.randint(1, 4)
            if index3 == 1:
                game_over_sudetenland()
            else:
                print_pause("We now have a choice, to either demand the "
                            "region of Danzig from Poland, which would put "
                            "us at war with the Allies, or we could ignore "
                            "Poland and just focus on the West.")
                west_or_east()
        elif "Anschluss" in items and "Rhineland" not in items:
            index3 = random.randint(1, 8)
            if index3 == 1:
                game_over_sudetenland()
            else:
                print_pause("We now have a choice, to either demand the "
                            "region of Danzig from Poland, which would put "
                            "us at war with the Allies, or we could ignore "
                            "Poland and just focus on the West.")
                west_or_east()
        elif "Anschluss" and "Rhineland" in items:
            print_pause("We now have a choice, to either demand the "
                        "region of Danzig from Poland, which would put "
                        "us at war with the Allies, or we could ignore "
                        "Poland and just focus on the West.")
            west_or_east()

    else:
        diktat_choice()


def cze_invasion_success():
    print("")
    items.append("Sudetenland")
    print_pause("The Czechs stood no chance against us.")
    print_pause("We can now concentrate our efforts to the Western front.")
    print_pause("But now we have a choice.")
    print_pause("Keep pushing Eastward and attack Poland, or focus on the "
                "West.")
    west_or_east()


def west_or_east():
    west_or_east_decision = valid_input('Ignore Poland or Danzig or War '
                                        '(1|2)\n', ['1', '2'])
    if west_or_east_decision == '1':
        print_pause("We choose to not focus on Poland right now.")
        print_pause("We choose to focus on the West.")
        operation_weserubung()
    elif west_or_east_decision == '2':
        danzig_or_war()
    else:
        west_or_east()


def danzig_or_war():
    print("")
    print_pause("We send the ultimatum to Poland!")
    index4 = random.randint(1, 6)
    if index4 == 1:
        print_pause("Poland accepts!")
        print_pause("Danzig is ours.")
        if "War" in items:
            items.append("Poland")
            operation_weserubung()
        else:
            print_pause("Due to our aggression in the East, the Allies "
                        "attack!")
            print_pause("We are now at war with Britain and France.")
            items.append("War")
            items.append("Poland")
            operation_weserubung()
    else:
        print_pause("The Poles refuse.")
        print_pause("We will launch our invasion soon.")
        molotov_ribbentrop()


def molotov_ribbentrop():
    print("")
    print_pause("But first, shall we form an alliance with the Soviets and "
                "cede Eastern Poland?")
    print_pause("This will give us a pact of non-aggression with them.")
    print_pause("This would be useful to avoid a 2 front war.")
    print_pause("Should we sign the pact?")
    molotov_ribbentrop_decision()


def molotov_ribbentrop_decision():
    molotov_ribbentrop_choice = valid_input('Sign the Pact or All of Poland '
                                            'is ours. (1|2)\n', ['1', '2'])
    if molotov_ribbentrop_choice == '1':
        print_pause("The pact has been signed.")
        items.append("West_Poland")
        if "War" not in items:
            print_pause("Because of our Eastern aggression, Britain and "
                        "France declare war!")
            print_pause("We are now at war with the Allies.")
            items.append("War")
        else:
            pass
        print_pause("Poland has been crushed by the two powers crashing down "
                    "on either side.")
        print_pause("We occupy the West, and the Soviets take the East.")
        operation_weserubung()

    elif molotov_ribbentrop_choice == '2':
        print_pause("We choose not to sign the pact.")
        if "Rhineland" in items:
            if "Anschluss" not in items:
                if "Sudetenland" not in items:
                    index5 = random.randint(1, 2)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()
                else:
                    index5 = random.randint(1, 5)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()
            else:
                if "Sudetenland" in items:
                    index5 = random.randint(1, 4)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()
                else:
                    index5 = random.randint(1, 2)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()

        elif "Rhineland" not in items:
            if "Anschluss" in items:
                if "Sudetenland" in items:
                    index5 = random.randint(1, 8)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()
                else:
                    index5 = random.randint(1, 5)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()
            else:
                if "Sudetenland" in items:
                    index5 = random.randint(1, 4)
                    if index5 == 1:
                        game_over_poland()
                    else:
                        print_pause("The Poles fight hard, but we still come"
                                    " out victorious in the end.")
                        items.append("Poland")
                        operation_weserubung()
                else:
                    game_over_poland()

                if index5 == 1:
                    game_over_poland()
                else:
                    print_pause("The Poles fight hard, but we still come out "
                                "victorious in the end.")
                    items.append("Poland")
                    operation_weserubung()

    else:
        molotov_ribbentrop_decision()


def operation_weserubung():
    print("")
    print_pause("Before we launch our invasion into France, we have an "
                "opportunity to launch an invasion into Denmark and Norway.")
    print_pause("The Allies are blocking our trade with Sweden, and we need "
                "to secure our resources.")
    print_pause("Should we commence the operation?")
    operation_weserubung_decision()


def operation_weserubung_decision():
    print("")
    print("1. Launch the invasion.")
    print("2. Scandinavia is a waste of our time.")
    print("Pick either '1' or '2'.")
    operation_weserubung_choice = valid_input('Launch the invasion or '
                                              'Scandinavia is a waste of time '
                                              '(1|2)\n', ['1', '2'])
    if operation_weserubung_choice == '1':
        items.append("iron_ore_surplus")
        print_pause("The invasion was a success!")
        print_pause("We have secured our trade with Sweden.")
        around_maginot_intro()
    elif operation_weserubung_choice == '2':
        items.append("Blockade")
        print_pause("We decide to do nothing, but now we suffer from the "
                    "British blockade.")
        around_maginot_intro()
    else:
        operation_weserubung_decision()


def around_maginot_intro():
    print("")
    print_pause("Now that the East is covered, we now focus our efforts to "
                "the West, and more specifically, the French.")
    print_pause("We have a choice. To invade through the Benelux countries, "
                "through Switzerland, or pierce through the French maginot.")
    print_pause("What shall we do?")
    around_maginot()


def around_maginot():
    around_maginot_decision = valid_input('Go through the Benelux, '
                                          'Switzerland, or straight through? '
                                          '(1|2|3)\n', ['1', '2', '3'])
    if around_maginot_decision == '1':
        if "Poland" or "West_Poland" in items:
            if "iron_ore_surplus" in items:
                benelux_victory()
            else:
                index6 = random.randint(1, 5)
                if index6 == 1:
                    game_over_benelux()
                else:
                    benelux_victory()
        else:
            if "iron_ore_surplus" in items:
                index6 = random.randint(1, 4)
                if index6 == 1:
                    game_over_benelux()
                else:
                    benelux_victory()

    elif around_maginot_decision == '2':
        if "Poland" or "West_Poland" in items:
            if "iron_ore_surplus" in items:
                swiss_victory()
            else:
                game_over_switzerland()
        elif "Anschluss" in items:
            if "iron_ore_surplus" in items:
                index6 = random.randint(1, 7)
                if index6 == 1:
                    game_over_switzerland()
                else:
                    print_pause("We have suffered heavy casualties in the "
                                "fight through Switzerland.")
                    print_pause("This will hurt us later on.")
                    items.append("Heavy_Casualties")
                    swiss_victory()
            else:
                game_over_switzerland()

    elif around_maginot_decision == '3':
        if "Poland" or "West_Poland" in items:
            if "Anschluss" and "Sudetenland" in items:
                if "iron_ore_surplus" in items:
                    french_victory()
                else:
                    index6 = random.randint(1, 4)
                    if index6 == 1:
                        game_over_france()
                    else:
                        print_pause("We have suffered heavy casualties in the "
                                    "fight through the French Maginot.")
                        print_pause("This will hurt us later on.")
                        items.append("Heavy_Casualties")
                        french_victory()
            else:
                game_over_france()
        else:
            if "Anschluss" and "iron_ore_surplus" and "Sudetenland" in items:
                index6 = random.randint(1, 11)
                if index6 == 1:
                    print_pause("We have suffered heavy casualties in the "
                                "fight through the French Maginot.")
                    print_pause("This will hurt us later on.")
                    items.append("Heavy_Casualties")
                elif index6 == 2:
                    game_over_france()
                else:
                    french_victory()
            else:
                game_over_france()
    else:
        around_maginot()


def benelux_victory():
    print("")
    print_pause("We decide to go around the Maginot through Belgium.")
    print_pause("Fortunately for us, our operation is a success!")
    print_pause("We breeze through the Benelux and the Allied forces are "
                "caught off guard!")
    print_pause("We are able to push through France and Paris is ours.")
    print_pause("France has fallen.")
    fall_of_france()


def french_victory():
    print("")
    print_pause("We decide to try to pierce the Maginot.")
    print_pause("Fortunately for us, our strength outweighs that of the "
                "Allies.")
    print_pause("We are able to push through France.")
    print_pause("Paris is ours and France has fallen.")
    fall_of_france()


def swiss_victory():
    print("")
    print_pause("We decide to go around the Maginot and through Switzerland.")
    print_pause("Fortunately for us, our operation is a success!")
    print_pause("We fight through the Alps and finish off Switzerland.")
    print_pause("We move through France with ease.")
    print_pause("Paris is ours and France has fallen.")
    fall_of_france()


def fall_of_france():
    print("")
    if ["Rhineland", "Anschluss", "Sudetenland", "iron_ore_surplus"] in items:
        if "West_Poland" or "Poland" in items:
            western_victory()
        else:
            war_continues()
    else:
        war_continues()


def western_victory():
    print_pause("After the fall of France, because of our sheer power, the "
                "United Kingdom has decided to sue for peace.")
    print_pause("Now that the Western War has come to an end, now we have "
                "the issue of the Soviet Union.")
    print_pause("The Soviets pose no current threat to us, but in order to "
                "fulfill German lebensraum, Soviet territories may be of use "
                "to us.")
    print_pause("Shall we invade, or declare victory?")
    end_game_decision()


def end_game_decision():
    pvdecision = valid_input('Invade or Declare victory? (1|2)\n', ['1', '2'])
    items.remove("War")
    if "Blockade" in items:
        items.remove("Blockade")
    else:
        pass
    if pvdecision == '1':
        print_pause("We have decided to launch our invasion of the Soviets.")
        operation_barbarossa()
    elif pvdecision == '2':
        partial_victory()
    else:
        end_game_decision()


def war_continues():
    print("")
    print_pause("After the fall of France, The United Kingdom has decided to "
                "continue the war.")
    print_pause("Now that France has fallen however, we have an opportunity "
                "to strike in the East.")
    print_pause("The Red Army has been weakened after Stalin's purges and "
                "this is our opportunity to take advantage.")
    print_pause("What shall we do?")
    op_bar_decision()


def op_bar_decision():
    op_bar_decision = valid_input('Invade the Soviets or Do nothing (1|2)\n',
                                  ['1', '2'])
    if op_bar_decision == '1':
        print_pause("We decide to invade.")
        operation_barbarossa()
    elif op_bar_decision == '2':
        print_pause("We decide to do nothing.")
        soviet_invasion()
    else:
        op_bar_decision()


def soviet_invasion():
    print_pause("Although we decided to stay neutral, the Soviets launch "
                "their own invasion!")
    if "War" in items:
        print_pause("In new world news, Japan has attacked Pearl Harbor.")
        print_pause("This now means the United States has joined the Allies.")
        print_pause("Rumor has it that they're planning an invasion into "
                    "France.")
        items.append("US")
    else:
        pass
    if "Blockade" in items:
        print_pause("Although we are initially able to hold them off, "
                    "eventually, our material shortages get the best of us.")
        game_over_soviets()
    else:
        index8 = random.randint(1, 3)
        if index8 == '1':
            print_pause("We are unable to hold the Russians back.")
            game_over_soviets()
        else:
            print_pause("Unfortunately for the Soviets, they are no match "
                        "for us.")
            print_pause("We are able to easily push the Red Army back.")
            barbarossa_victory()


def operation_barbarossa():
    print("")
    print_pause("The Red Army is caught off guard!")
    print_pause("We push easily through Ukraine and Belarus.")
    print_pause("Unfortunately though, it feels like Soviet resistance keeps "
                "hardening the futher we push.")
    if "War" in items:
        print_pause("In new world news, Japan has attacked Pearl Harbor.")
        print_pause("This now means the United States has joined the Allies.")
        print_pause("Rumor has it that they're planning an invasion into "
                    "France.")
        items.append("US")
    else:
        pass
    if "Blockade" in items:
        print_pause("It seems that we are being successfully held in our "
                    "advances.")
        print_pause("Due to British and French blockades, we do not have "
                    "access to the resources to sustain this invasion.")
        print_pause("We are being pushed back!")
        print_pause("The Soviets have mobilized and outnumber us.")
        print_pause("The Soviet Union takes Warsaw and pushes to Berlin.")
        print_pause("The Allies land in France to little resistance and push "
                    "inland.")
        print_pause("Game Over")
        play_again()
    else:
        if "Heavy_Casualties" in items:
            print_pause("It seems that we are being successfully held in our "
                        "advances.")
            print_pause("Because of heavy losses from our Western wars, we "
                        "are unable to sustain an Eastern invasion.")
            print_pause("The Soviets easily mobilize, outnumber, and push "
                        "us back.")
            if "War" and "US" in items:
                print_pause("The Soviet Union takes Warsaw and pushes to "
                            "Berlin.")
                print_pause("The Allies land in France to little resistance "
                            "and push inland.")
                print_pause("Game Over")
                play_again()
            elif "War" in items and "US" not in items:
                print_pause("The Soviet Union takes Warsaw and pushes "
                            "through Germany.")
                print_pause("Game Over")
                play_again()
            elif "War" not in items:
                index7 = random.randint(1, 4)
                if index7 == 1:
                    print_pause("The Soviet Union takes Warsaw and pushes "
                                "through Germany.")
                    print_pause("Game Over")
                    play_again()
                else:
                    barbarossa_victory()
        else:
            if "War" and "US" in items:
                index7 = random.randint(1, 6)
                if index7 == 1:
                    barbarossa_victory()
                else:
                    print_pause("Back in the East, the Soviets have "
                                "mobilized and outnumber us.")
                    print_pause("We are now being pushed back.")
                    print_pause("The Allies land in France to little "
                                "resistance and push inland.")
                    print_pause("The Soviet Union takes Warsaw and pushes "
                                "to Berlin.")
                    print_pause("Game Over")
                    play_again()
            elif "War" in items and "US" not in items:
                index7 = random.randint(1, 4)
                if index7 == 1:
                    barbarossa_victory()
                else:
                    print_pause("Back in the East, the Soviets have "
                                "mobilized and outnumber us.")
                    print_pause("We are now being pushed back.")
                    print_pause("The Soviet Union liberates Warsaw and "
                                "pushes through Germany.")
                    print_pause("Game Over")
                    play_again()
            else:
                barbarossa_victory()


def game_over_anschluss():
    print("")
    print_pause("Disaster has struck!")
    print_pause("Austria has called on its Allies; the United Kingdom, "
                "France, and Italy to come to its protection!")
    print_pause("Due to our military weakness, we crumble.")
    print_pause("The Third Reich has come to an end.")
    play_again()


def game_over_sudetenland():
    print("")
    print_pause("The Allies notice our weaknesses and decide to invade to "
                "protect democracy in Europe.")
    print_pause("We are unable to hold them back.")
    print_pause("Berlin has fallen.")
    play_again()


def game_over_poland():
    print("")
    print_pause("We launch our invasion of Poland anyways.")
    if "War" in items:
        print_pause("Because of our invasion, Britain and France declare "
                    "war!")
    else:
        pass
    print_pause("We are too weak! The Poles hold us back while the Allies "
                "push from the West!")
    print_pause("Our military has been disintigrated.")
    print_pause("We have been defeated.")
    play_again()


def game_over_benelux():
    print("")
    print_pause("We decide to repeat our World War 1 strategy and smash "
                "through Belgium.")
    print_pause("Unfortunately, the Allies were prepared and studied our "
                "weaknesses.")
    print_pause("The Dutch and Belgians hold us back long enough for the "
                "Allies to arrive.")
    print_pause("The coalition pushes us back.")
    print_pause("Game Over")
    play_again()


def game_over_switzerland():
    print("")
    print_pause("We decide to go around the Maginot and through Switzerland.")
    print_pause("Unfortunately, the Allies were prepared and studied our "
                "weaknesses.")
    print_pause("We are not prepared to cross the Swiss Alps, and the "
                "trained Swiss army is able to push us back.")
    print_pause("Game Over")
    play_again()


def game_over_france():
    print("")
    print_pause("We have decided to try to pierce the French Maginot.")
    print_pause("Unfortunately, the area was too fortified and we're stuck.")
    print_pause("We suffer heavy losses and the Allies are able to push us "
                "back.")
    print_pause("Game Over")
    play_again()


def game_over_soviets():
    print_pause("The Soviets keep pushing us back.")
    if "US" in items:
        print_pause("The Allies land in France to little resistance.")
        print_pause("They push from the West while the Soviets push from "
                    "the East.")
        print_pause("The Soviet Union takes Warsaw and keeps pushing to "
                    "Berlin.")
        print_pause("The Allies liberate West Germany.")
        print_pause("Game Over")
        play_again()


def partial_victory():
    print("")
    print_pause("We have decided to end the wars and begin rebuilding.")
    print_pause("We have successfully consolidated our position in Europe.")
    print_pause("We are content with a second superpower and establish "
                "positive diplomatic relations.")
    print_pause("We have won.")
    play_again()


def barbarossa_victory():
    print("")
    print_pause("We have breezed through the Soviet Union.")
    print_pause("They have fallen.")
    if "War" in items:
        print_pause("After our victory in the East, the Allies have all "
                    "decided to sue for peace.")
    else:
        pass
    print_pause("We are now the only dominant continental superpower.")
    print_pause("We have won.")
    play_again()


def play_game():
    intro()
    rhineland_intro()
    anschluss_intro()


def play_again():
    play_again = valid_input('Would you like to play again? (yes|no)\n',
                             ['yes', 'no'])
    if play_again == 'yes':
        items.clear()
        print("")
        play_game()


play_game()
