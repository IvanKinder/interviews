import json
import os
import sys


class History:

    def __init__(self):
        self.history_arr = []
        self.score = 1
        self.iterator = 0
        self.dubles = 0

    def set_history(self, sequence: list, score: float):
        self.iterator = 0
        if self.is_it_dupe_sequence(sequence):
            self.dubles += self.iterator
            if score < self.score:
                self.score = score
            return self.iterator
        else:
            for num in sequence:
                self.history_arr.append(num)
            return 0

    def is_it_dupe_sequence(self, sequence: list):
        self.iterator = 0
        for i in range(len(self.history_arr) - len(sequence) + 1):
            tmp = self.history_arr[i:i + len(sequence)]
            if tmp == sequence:
                self.iterator += 1
        if self.iterator != 0:
            return True
        else:
            return False

    def save_history(self, filepath: str):
        my_dir = sys.path[0]
        if filepath:
            os.chdir(filepath)
        data = {'history_arr': self.history_arr, 'score': self.score}
        with open(f'history.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
        os.chdir(my_dir)

    @staticmethod
    def load_history(filepath: str):
        if filepath:
            os.chdir(filepath)
        with open(f'history.json', 'r', encoding='utf-8') as file:
            hist_obj = History()
            data = json.load(file)
            hist_obj.history_arr = data['history_arr']
            hist_obj.score = data['score']
            return hist_obj
