import unittest

from direct.showbase.ShowBase import ShowBase

class MinimalExampleGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.value = 'green'
        self.accept('turn-blue', self.update_value, ['blue'])
        self.accept('turn-red', self.update_value, ['red'])

    def update_value(self, newValue):
        self.value = newValue
        
        
   
class TestsMinimalExample(unittest.TestCase):
    def test_initial_value(self):
        desired = 'green'
        testGame = MinimalExampleGame()
        result = testGame.value
        self.assertEqual(desired, result)
        
    def test_event_turn_blue_changes_value(self):
        desired = 'blue'
        testGame = MinimalExampleGame()
        testGame.messenger.send('turn-blue')
        result = testGame.value
        testGame.destroy()
        self.assertEqual(desired, result)
        
    def test_event_turn_red_changes_value(self):
        desired = 'red'
        testGame = MinimalExampleGame()
        testGame.messenger.send('turn-red')
        result = testGame.value
        testGame.destroy()
        self.assertEqual(desired, result)

if __name__ == '__main__':
    unittest.main()