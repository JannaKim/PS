
#include <stdio.h>
#include <vector>
#include <iomanip>
#include <iostream>
using namespace std;
int main()
{
    vector<double> ans_list;

    int n_case;
    scanf("%d", &n_case);
    while (n_case--)
    {
        int n;
        vector<double> scores;
        scanf("%d", &n);

        int sum = 0;
        for (int i = 0; i < n; i++) //input
        {
            int score;
            scanf("%d", &score);
            scores.push_back(score);
            sum += score;
        }

        //typedef vector<double>::size_type vsz; //이게 auto
        //auto sc_size = scores.size();
        //cout<<sc_size<<endl;

        //double avg=1.f*sum/N;
        double avg = (double)sum / n;

        int cnt = 0;

        for (const auto &sc : scores)
        {
            if (sc > avg)
                cnt++;
        }
        // op + shift+f
        /*
        vector<double> scores_above_avg;
        for (const auto &score : scores) // for el in L
        {
            if (score > avg)
                scores_above_avg.push_back(score);
        }


        for (const auto score : scores_above_avg)
            cout << score;
        cout << "\n";
        */

        ans_list.push_back((double)cnt / n);

        /*
    std::copy_if(all_items.begin(), all_items.end(), std::back_inserter(filter_items),
             [&bad_ids](const mystruct& item)
{
     return std::find(bad_ids.begin(), bad_ids.end(), item.id) == bad_ids.end();
});
*/
    } //test cases end
    for (const auto &ans : ans_list)
    {
        printf("%.3lf%%\n", ans*100);
    }

    return 0;
}













    /*
    for (int i = 0; i < n_case; i++)
    {
        printf("%.3lf%%\n", ans_list[i]); //% 기호 자체 출력: 2개 중복해줘야 한다.
    }
*/
    //sc_list 출력

    //cout<<ans.begin()<<' '<<ans.end()<<endl;
    //printf("%d %d",ans.begin(), ans.end());

/*
    printf("%lf,%lf", ans_list.front(), ans_list.back());

    cout << "********************\n";
    sort(ans_list.begin(), ans_list.end());
    cout << '\n';
    for (vector<double>::iterator i = ans_list.begin(); i != ans_list.end(); i++)
    {
        cout << *i << " ";
    }
    cout << '\n';
    vector<double>::reverse_iterator ir(ans_list.rbegin());
    for (; ir != ans_list.rend(); ++ir) // 뒤에서부터 출력
    {                                   // ans.rend()포함 안하고 돌리나?
        cout << *ir << " ";
    }

*/