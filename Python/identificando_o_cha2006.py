class TeaCompetition:
    def __init__(self, target_tea):
        self._target_tea = target_tea
        self._correct_count = 0

    def check_answers(self, answers_list):
        self._correct_count = 0
        for answer in answers_list:
            if answer == self._target_tea:
                self._correct_count += 1
    
    def get_result(self):
        return self._correct_count


class App:
    @staticmethod
    def run():
        try:
            target = int(input())
            answers = [int(x) for x in input().split()]

            competition = TeaCompetition(target)
            competition.check_answers(answers)

            print(competition.get_result())
            
        except (ValueError, EOFError):
            pass

if __name__ == "__main__":
    App.run()