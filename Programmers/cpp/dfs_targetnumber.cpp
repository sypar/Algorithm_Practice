#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int target) {
    if (numbers.size()==0 && target==0) {
        return 1;
    }
    else if (numbers.size() == 0) {
        return 0;
    }

    int temp = numbers[0];
    numbers.erase(numbers.begin());

    return solution(numbers, target + temp) + solution(numbers, target - temp);
}

int main(){
    vector<int> numbers(5,1);
    solution(numbers,3);
    return 0;
}