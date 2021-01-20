#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <math.h>
#include <ctime>
/* -----------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------- Pretreatement area ---------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------- */

/* ------------------------------------------ GET COMMAND ------------------------------------------ */
#define GETV(V,n)					tools::vectors::getVector(&V, n);
#define GETNK						cin>>N>>K
#define GETS						cin>>avp[0]>>avp[1]
/* ------------------------------------------ PRINT ------------------------------------------ */
#define PRINT(V)					tools::printing::printing_cleaned_vector_instance_with_blank(V);
#define endll						"\n"
/* ------------------------------------------ UTILITY ------------------------------------------ */
#define fori(a)						for(int i=0;i<a;i++)
#define forj(a)						for(int j=0;j<a;j++)
#define fork(a)						for(int k=0;k<a;k++)
#define IS_SMALL_ALPHA(a)			((a>='a')&&(a<='z'))
#define IS_BIG_ALPHA(a)				((a>='A')&&(a<='Z'))
#define IS_SMALL_VOWEL(a)			((a=='a')||(a=='e')||(a=='i')||(a=='o')||(a=='u'))
#define IS_BIG_VOWEL(a)				((a=='A')||(a=='E')||(a=='I')||(a=='O')||(a=='U'))
#define IS_NUMBER(a)				((a>='0')&&(a<='9'))
#define MAXS(a,b)					((a>b)?a:b)
#define MINS(a,b)					((a<b)?a:b)
#define ALP							'z'-'a'+1
#define FILL_ASCEND(v,n)			fori(n)v[i]=i;
#define FILL_INIT(v,k)				fill(v.begin(), v.end(), k)		
#define SORT(V)						sort(V.begin(), V.end());
#define SORT_COMP(V,c)				sort(V.begin(), V.end(),c);
#define GCD(a,b)					tools::utilities::gcd(a,b)
#define LCM(a,b)					tools::utilities::lcm(a,b)
#define IN_RANGE(x,y,X1,Y1,X2,Y2)	((x>=X1)&&(x<=X2)&&(y>=Y1)&&(y<=Y2))
#define IS_SIGNED(x)				((x>0)?1:((x==0)?0:-1))
/* ------------------------------------------ CONSTANTS  ------------------------------------------ */
#define PI							atan(1)*4
/* ------------------------------------------ DEBUGGING ------------------------------------------ */
#define ctab(a)						DD tools::printing::print_tab(a)
#define ttt							puts("test");
#define DD							if(DEBUG)
#define dcout						DD cout
#define TIMES(n)					timetag[n] = clock();
#define TIME_GAP(a,b)				((double)(timetag[b]-timetag[a])/1000)

/* -----------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------ default area ------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------- */
using namespace std;

namespace page {
	typedef			unsigned long long int		ulint;
	typedef			signed long long int		lint;
	typedef			vector<int>					vint;
	typedef			vector<double>				dint;
	typedef			vector<string>				sint;
	lint			T, N, M, K, R, C, Q, P, W, V;
	lint			avp[50];
	string			stx;
	int				dirx[4][2] = { { 1,0 },{ 0,1 },{ -1,0 },{ 0,-1 } };
	time_t			timetag[50];
}using namespace page;
namespace tools {
	class point {
	public:
		int x;
		int y;
		point() {
			this->x = 0;
			this->y = 0;
		}
		point(int x_, int y_) {
			this->x = x_;
			this->y = y_;
		}
		void setCoordinate(int x_, int y_) {
			this->x = x_;
			this->y = y_;
		}
	};
	point make_point(int x, int y) {
		point p(x, y);
		return p;
	}
	namespace vectors {
		template <typename T>
		double average(vector<T> v) {
			if (v.empty())return 0;
			double av = 0;
			for (int i = 0; i < v.size(); i++)
				av += (double)v[i];
			return av / v.size();
		}
		vector<int> intstring_to_vector(string str) {
			vector<int> ps;
			for (int i = 0; i < str.length(); i++)
				ps.push_back(str[i] - '0');
			return ps;
		}
		vector<int> integer_split_to_vector(int num) {
			vector<int> tmp;
			for (; num != 0; num /= 10)
				tmp.insert(tmp.begin(), num % 10);
			return tmp;
		}
		template <typename T>
		vector<T> max_of_vector(vector<T> tnum, T min) {
			//index 0 is max value, index 1 is max value index
			vector<T> vlin(2);
			T max = min, index = -1;
			for (int i = 0; i < tnum.size(); i++) {
				if (max < tnum[i]) {
					max = tnum[i];
					index = i;
				}
			}
			vlin[0] = max;
			vlin[1] = index;
			return vlin;
		}
		template <typename T>
		vector<T> min_of_vector(vector<T> tnum, T max) {
			//index 0 is max value, index 1 is max value index
			vector<T> vlin(2);
			T min = max, index = -1;
			for (int i = 0; i < tnum.size(); i++) {
				if (min > tnum[i]) {
					min = tnum[i];
					index = i;
				}
			}
			vlin[0] = min;
			vlin[1] = index;
			return vlin;
		}
		template <typename T>
		vector<T> array_to_vector(T* t, size_t start, size_t size) {
			vector<T> tvex;
			for (size_t i = 0; i < size; i++)
				tvex.push_back(t[start + i]);
			return tvex;
		}
		template <typename T>
		T sum_of_vector(vector<T>t) {
			T tn = (T)0;
			for (int i = 0; i < t.size(); i++)
				tn += t[i];
			return tn;
		}
		template <typename T>
		void getVector(vector<T> *tx, int num) {
			T p;
			for (int i = 0; i < num; i++) {
				cin >> p;
				(*tx).push_back(p);
			}
		}
	}
	namespace strings {
		string substring(string str, size_t start, size_t end) {
			if (start > str.length() - 1)return "";
			if (end < 0)return "";
			if (start < 0) {
				if (end > str.length() - 1) {
					cout << "start, end : OUT OF RANGE" << endl;
					return str;
				}
				cout << "start : OUT OF RANGE" << endl;
				start = 0;
			}
			if (end > str.length() - 1) {
				end = str.length() - 1;
				cout << "end : OUT OF RANGE" << endl;
			}
			return str.substr(start, end - start + 1);
		}
		string reverse_string(string str) {
			string str2 = "";
			for (int i = str.length() - 1; i >= 0; i--)
				str2 = str2 + str[i];
			return str2;
		}
	}
	namespace utilities {
		namespace engine {
			vector<int> source;
			vint PrimeSource;
			bool isPrimeDetail(int n) {
				if (n == 2)return true;
				for (int i = 0; i<source.size(); i++) {
					if (source[i] > sqrt(n)) break;
					if (n%source[i] == 0)return false;
				}
				return true;
			}
			void getSource(int end_interval) {
				if (end_interval < 2)return;
				source.clear();
				for (int i = 2; i < end_interval; i++) {
					if (isPrimeDetail(i))source.push_back(i);
				}
			}
			bool isSource_DetailFinder(int start, int end, int n) {
				if (end < start)return false;
				int mid = (start + end) / 2;
				if (n == source[mid])return true;
				if (n < source[mid])
					return isSource_DetailFinder(start, mid - 1, n);
				return isSource_DetailFinder(mid + 1, end, n);
			}
			void getPrimeSource(int n) {
				//FAST in single test
				if (n == 1)return;
				vector<int> v;
				for (int i = 2; i <= n; i++)
					v.push_back(i);
				v.push_back(n);
				while (true) {
					if (v.size() == 0)return;
					int first_one = v[0];
					PrimeSource.push_back(first_one);
					for (vector<int>::iterator iter = v.begin(); iter != v.end();) {
						if ((*iter) % first_one == 0) iter = v.erase(iter);
						else iter++;
					}
				}
			}
		}
		template <typename T>
		void swap(T* a, T* b) {
			T vr = *a;
			*a = *b;
			*b = vr;
		}
		bool isPrimeNumber_Eratostenes(int n) {
			//FAST in single test
			if (n == 1)return false;
			vector<int> v;
			for (int i = 2; i <= sqrt(n); i++)
				v.push_back(i);
			v.push_back(n);
			while (true) {
				if (v.size() == 0)return false;
				if (v[v.size() - 1] != n)return false;
				if (v[0] == n)return true;
				int first_one = v[0];
				for (vector<int>::iterator iter = v.begin(); iter != v.end();) {
					if ((*iter) % first_one == 0) iter = v.erase(iter);
					else iter++;
				}
			}
		}
		bool isPrimeNumber_Custom(int n) {
			//FAST in sequence test
			if ((engine::source.size() == 0) || (engine::source[engine::source.size() - 1]<n))
				engine::getSource(n);
			return engine::isSource_DetailFinder(0, engine::source.size() - 1, n);
		}
		ulint gcd(ulint a, ulint b) {
			return b == 0 ? a : gcd(b, a % b);
		}
		ulint lcm(ulint a, ulint b) {
			ulint g = gcd(a, b);
			return g * (a / g)*(b / g);
		}
		string integer_to_string(int integer) {
			return to_string(integer);
		}
		int string_to_integer(string str) {
			return atoi(str.c_str());
		}
		int semi_floor(double d) {
			return floor(d + 0.5);
		}
		namespace bit {
			void clean_zero_bit_string(string* str) {
				string str2 = *str;
				while (true) {
					if (str2.length() == 1)break;
					if (str2[0] != '0')break;
					str2.erase(str2.begin());
				}
				*str = str2;
			}
			ulint numX_to_num10_ulinteger(string s, int X) {
				ulint k = 0;
				for (int i = s.length() - 1; i >= 0; i--) {
					if (IS_BIG_ALPHA(s[i]))
						k += (s[i] - 'A')*pow(X, s.length() - 1 - i);
					else if (IS_SMALL_ALPHA(s[i]))
						k += (s[i] - 'a')*pow(X, s.length() - 1 - i);
					else if (IS_NUMBER(s[i]))
						k += (s[i] - '0')*pow(X, s.length() - 1 - i);
				}
				return k;
			}
			string numX_to_num10_string(string s, int X) {
				int k = 0;
				for (int i = s.length() - 1; i >= 0; i--) {
					if (IS_BIG_ALPHA(s[i]))
						k += (s[i] - 'A')*pow(X, s.length() - 1 - i);
					else if (IS_SMALL_ALPHA(s[i]))
						k += (s[i] - 'a')*pow(X, s.length() - 1 - i);
					else if (IS_NUMBER(s[i]))
						k += (s[i] - '0')*pow(X, s.length() - 1 - i);
				}
				return integer_to_string(k);
			}
			string num10_integer_to_numX(ulint number, ulint X) {
				string str = "";
				for (; number != 0; number /= X) {
					ulint converted = number % X;
					char c;
					if (converted > 9)
						c = (number % X) + 'A' - 10;
					else
						c = (number % X) + '0';
					string sss(1, c);
					str = sss + str;
				}
				return str;
			}
			string num10_string_to_numX(string str2, int X) {
				int number = string_to_integer(str2);
				string str = "";
				for (; number != 0; number /= X) {
					int converted = number % X;
					char c;
					if (converted > 9)
						c = (number % X) + 'A' - 10;
					else
						c = (number % X) + '0';
					string sss(1, c);
					str = sss + str;
				}
				return str;
			}
			string numX_to_numY(string str, int X, int Y) {
				return num10_string_to_numX(numX_to_num10_string(str, X), Y);
			}
		}
	}
	namespace printing {
		void print_tab(int n) {
			for (int i = 0; i < n; i++)
				cout << "\t";
		}
		template <typename T>
		void printing_vector_instance(string str, vector<T> tt) {
			cout << str << " [size = " << tt.size() << "] -> ";
			for (int i = 0; i < tt.size(); i++)
				cout << "[" << tt[i] << "] ";
			cout << endl;
		}
		template <typename T>
		void printing_cleaned_vector_instance_with_blank(vector<T> tt) {
			for (int i = 0; i < tt.size(); i++)
				cout << tt[i] << " ";
			cout << endl;
		}
		template <typename T>
		void printing_cleaned_vector_instance_with_newline(vector<T> tt) {
			for (int i = 0; i < tt.size(); i++)
				cout << tt[i] << endl;
		}
	}
	namespace environment {
		void INITIAL_SETTING_FOR_OPTIMIZING() {
			cin.tie(NULL);
			ios::sync_with_stdio(false);
			/* Don't use scanf, printf, puts, getchar, putchar in submission */
		}
	}
}using namespace tools;

/* -----------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------- MAIN area --------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------- */

const bool DEBUG = 0;
/* -------------------------------------------- CUSTOM -------------------------------------------- */

int main() {
	tools::environment::INITIAL_SETTING_FOR_OPTIMIZING(); 	//DEFAULT
	/* -------------------------------------------- CUSTOM -------------------------------------------- */
	vint v;
	GETNK;
	GETV(v, N);
	SORT(v);
	cout << v[K - 1] << endll;
}