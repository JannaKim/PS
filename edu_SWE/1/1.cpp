extern void doUserImplementation(int guess[])
{
    int Num_Idx = 0;
    int list[5040];
    bool chk[9877];

    for (int i = 123; i <= 9876; i++)
    {
        int fst = i / 1000;
        int snd = i % 1000 / 100;
        if (fst == snd) continue;

        int trd = i % 100 / 10;
        if (fst == trd || snd == trd) continue;

        int fth = i % 10;
        if (fst == fth || snd == fth || trd == fth) continue;

        list[Num_Idx++] = i;
    }

    for (int i = 0; i < Num_Idx; i++)
    {
        chk[list[i]] = true;
    }

    while (1)
    {
        int Candidate_Num;
        for (int i = 0; i < Num_Idx; i++)
        {
            if (chk[list[i]] == true)
            {
                Candidate_Num = list[i];
                guess[0] = Candidate_Num / 1000;
                guess[1] = Candidate_Num % 1000 / 100;
                guess[2] = Candidate_Num % 100 / 10;
                guess[3] = Candidate_Num % 10;
                break;
            }
        }

        Result r = query(guess);

        if (r.hit == 4) break;
        else chk[Candidate_Num] = false;

        for (int i = 0; i < Num_Idx; i++)
        {
            if (chk[list[i]] == true)
            {
                int temp1 = Candidate_Num;
                int temp2 = list[i];

                Result tmp = { 0, 0 };
                int arr[10];
                for (int i = 0; i < 10; i++) arr[i] = 0;

                for (int i = 0; i < 4; i++)
                {
                    if (temp1 % 10 == temp2 % 10) tmp.hit++;
                    else
                    {
                        arr[temp1 % 10]++;
                        arr[temp2 % 10]++;
                    }

                    if (arr[temp1 % 10] == 2) tmp.miss++;
                    if (arr[temp2 % 10] == 2) tmp.miss++;

                    temp1 = temp1 / 10;
                    temp2 = temp2 / 10;
                }

                if (r.hit != tmp.hit || r.miss != tmp.miss) chk[list[i]] = false;
            }
        }
    }
}