# encoding: UTF-8

class Actionwords:
    def __init__(self, test):
        self.test = test

    def i_start_the_coffee_machine_using_language_lang(self, lang = "en"):
        # TODO: Implement action: "Start the coffee machine using language %s" % (lang)
        raise NotImplementedError

    def i_shutdown_the_coffee_machine(self):
        # TODO: Implement action: "Shutdown coffee machine"
        raise NotImplementedError

    def message_message_should_be_displayed(self, message = ""):
        # TODO: Implement result: "Displayed message is \"%s\"" % (message)
        raise NotImplementedError

    def coffee_should_be_served(self):
        # TODO: Implement result: "Coffee is served :)"
        raise NotImplementedError

    def coffee_should_not_be_served(self):
        # TODO: Implement result: "No coffee is served :("
        raise NotImplementedError

    def i_take_a_coffee(self):
        # TODO: Implement action: "Take a coffee"
        raise NotImplementedError

    def i_empty_the_coffee_grounds(self):
        # TODO: Implement action: "Empty coffee grounds"
        raise NotImplementedError

    def i_fill_the_beans_tank(self):
        # TODO: Implement action: "Fill beans"
        raise NotImplementedError

    def i_fill_the_water_tank(self):
        # TODO: Implement action: "Fill water tank"
        raise NotImplementedError

    def i_take_coffee_number_coffees(self, coffee_number = 10):
        pass

    def the_coffee_machine_is_started(self):
        self.i_start_the_coffee_machine_using_language_lang()

    def i_handle_everything_except_the_water_tank(self):
        self.i_handle_coffee_grounds()
        self.i_handle_beans()

    def i_handle_water_tank(self):
        pass

    def i_handle_beans(self):
        pass

    def i_handle_coffee_grounds(self):
        pass

    def i_handle_everything_except_the_beans(self):
        self.i_handle_water_tank()
        self.i_handle_coffee_grounds()

    def i_handle_everything_except_the_grounds(self):
        self.i_handle_water_tank()
        self.i_handle_beans()

    def displayed_message_is(self, free_text = ""):
        self.message_message_should_be_displayed(message = __free_text)

    def i_switch_to_settings_mode(self):
        pass

    def settings_should_be(self, datatable = "||"):
        pass
