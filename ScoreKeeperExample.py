import unittest

from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase

class ScoreKeeper(DirectObject):
    def __init__(self):
        self.score = 0
        self.accept('score-change', self.update_score)
        
    def update_score(self, amount):
        self.score += amount
        
        
        
class ScoreKeeperExampleGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scoreKeeper = ScoreKeeper()
        
    def destroy(self):
        self.scoreKeeper.ignore_all()
        ShowBase.destroy(self)
        
        
   
class TestsScoreKeeperGame(unittest.TestCase):
    def test_initial_score(self):
        desired = 0
        testGame = ScoreKeeperExampleGame()
        result = testGame.scoreKeeper.score
        testGame.destroy()
        self.assertEqual(desired, result)
        
    def test_event_score_increases_once(self):
        desired = 50
        testGame = ScoreKeeperExampleGame()
        testGame.messenger.send('score-change', [50])
        result = testGame.scoreKeeper.score
        testGame.destroy()
        self.assertEqual(desired, result)
        
    def test_event_score_increases_twice(self):
        desired = 40
        testGame = ScoreKeeperExampleGame()
        testGame.messenger.send('score-change', [30])
        testGame.messenger.send('score-change', [10])
        result = testGame.scoreKeeper.score
        testGame.destroy()
        self.assertEqual(desired, result)        

    def test_event_score_decreases_once(self):
        desired = -25
        testGame = ScoreKeeperExampleGame()
        testGame.messenger.send('score-change', [-25])
        result = testGame.scoreKeeper.score
        testGame.destroy()
        self.assertEqual(desired, result)
        
    def test_event_score_increases_and_decreases(self):
        desired = 19
        testGame = ScoreKeeperExampleGame()
        testGame.messenger.send('score-change', [16])
        testGame.messenger.send('score-change', [-8])
        testGame.messenger.send('score-change', [14])
        testGame.messenger.send('score-change', [-3])
        result = testGame.scoreKeeper.score
        testGame.destroy()
        self.assertEqual(desired, result)
        
        

if __name__ == '__main__':
    unittest.main()