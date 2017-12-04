import sys
sys.path.append('/Users/dwd/go/src/github.com/user/numb')

from pyhooks.hooks import numb_test_result

from lenet import LeNet
# I am making change
model = LeNet() # chaaaaange!

numb_test_result({
    "accuracy": 2,
    "note": "trying out"
})