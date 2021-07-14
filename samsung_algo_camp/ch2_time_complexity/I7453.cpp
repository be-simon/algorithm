#include <cstdio>
#include <vector>
#include <algorithm> 
using namespace std;
typedef long long LL;

int n;
vector<int> a, b, c, d;
vector<int> ab, cd;

LL st1() {
    // 전략 1. 정렬 없이 바로 map 사용
}

LL st2_1() {
    // 전략 2. 정렬 ==>
    // 전략 2-1. lower_bound, upper_bound 
    sort(ab.begin(), ab.end());
    sort(cd.begin(), cd.end());
}

LL st2_2() {
    LL res = 0, cnt = 0;
    // 전략 2. 정렬 ==>
    // 전략 2-2. 안쓰고 ==> 
    sort(ab.begin(), ab.end());
    sort(cd.begin(), cd.end());
    int p_cd = cd.size() - 1;
    for (int p_ab = 0 ; p_ab < ab.size() ; p_ab++) {
        int target = -ab[p_ab];
        if (0 < p_ab && ab[p_ab] == ab[p_ab - 1]) {
            res += cnt;
        }
        else {
            while (0 <= p_cd && target < cd[p_cd]) {
                p_cd--;
            }
            cnt = 0;
            while (0 <= p_cd && target == cd[p_cd]) {
                cnt++;
                p_cd--
            }
            res += cnt;
        }
    }
    return res;
}

/*
LL st2_2() {
    LL res = 0, cnt = 0;
    // 전략 2. 정렬 ==>
    // 전략 2-2. 안쓰고 ==> 
    sort(ab.begin(), ab.end());
    sort(cd.begin(), cd.end());
    int p_cd = cd.size() - 1;
    for (int p_ab = 0 ; p_ab < ab.size() ; p_ab++) {
        if (0 < p_ab && ab[p_ab - 1] == ab[p_ab]) {
            res += cnt;
        }
        else {
            cnt = 0;
            while (0 <= p_cd && -ab[p_ab] < cd[p_cd]) p_cd--;
            while (0 <= p_cd && -ab[p_ab] == cd[p_cd]) cnt++, p_cd--;
            res += cnt; 
        }
    }
    return res;
}
*/

int main() {
    scanf("%d", &n);
    for (int i = 0 ; i < n ; i++) {
        int u, v, w, x;
        scanf("%d%d%d%d", &u, &v, &w, &x);
        a.push_back(u);
        b.push_back(v);
        c.push_back(w);
        d.push_back(x);
    }
    // a,b 로 만들수 있는 합의 조합 ==> ab
    // c,d로 만들수 있는 합의 조합 ==> cd
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j < n ; j++) {
            ab.push_back(a[i] + b[j]);
            cd.push_back(c[i] + d[j]);
        }
    }

    //printf("%lld", st_1());
    //printf("%lld", st_2_1());
    printf("%lld", st2_2());
}