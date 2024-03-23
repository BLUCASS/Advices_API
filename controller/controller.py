class Advice:
    """This class will manage the advices given to the users."""
    def __keep_going(self) -> int:
        """This method will force the user to answer the question properly."""
        while True:
            try:
                keep_going = str(input('Do you want to get a new advice? [Y/N]: ')).upper()[0]
                if keep_going != 'Y' and keep_going != 'N': raise ValueError
            except:
                print('\033[31mTO MAKE IT MORE INTERESTING, PLEASE FOLLOW THE RULES.\033[m')
            else: 
                return keep_going

    def __wanna_save(self) -> str:
        """This method will force the user to answer the question properly."""
        while True:
            try:
                save = str(input(
                    'Do you want to save this advice for later? [Y/N]: ')).upper()[0]
                if save != 'Y' and save != 'N': raise ValueError
            except:
                print('\033[31mTO MAKE IT MORE INTERESTING, PLEASE FOLLOW THE RULES.\033[m')
            else: 
                return save

    def __save_it(self, id, given_advice) -> dict:
        """If the method self.__wanna_save() is answered with 'Y', it will
        save the advice into a dictionary and returns it, else, it returns 'N'."""
        advices_kept = {}
        wanna_save = self.__wanna_save()
        if wanna_save == 'Y':
            advices_kept["id"] = id
            advices_kept["text"] = given_advice
            return advices_kept
        return 'N'

    def __consume_api(self) -> dict:
        """This method gets the json from the api and returns it."""
        import requests
        link = 'https://api.adviceslip.com/advice'
        response = requests.get(link)
        response = response.json()
        return response

    def get_advice(self) -> None:
        """This method will manage the user's interaction, calling the methos for
        answering and saving it. At the end, it will call a private method to
        print all the saved advices."""
        from time import sleep
        c = 1
        kept_advices = []
        while True:
            response = self.__consume_api()
            print(f'\033[1;42m{"NUM.":<5}{"ADVICE":^100}\033[m')
            print(f'{c:<5}{response["slip"]["advice"]:<100}')
            sleep(2)
            one_more = self.__keep_going()
            save_it = self.__save_it(c, response["slip"]["advice"])
            if save_it != 'N': kept_advices.append(save_it)
            c += 1
            if one_more == 'N': break
        self.__print_advices(kept_advices)

    def __print_advices(self, kept_advices) -> None:
        """This private method will only receives the advices as a list and 
        print them for the user."""
        print(f'\033[1;43m{"NUM.":<5}{"SAVED ADVICES":^100}\033[m')
        [print(f'{advice["id"]:<5}{advice["text"]:<100}') for advice in kept_advices]
