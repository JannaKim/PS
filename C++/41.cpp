#include <iostream>
#include <string>

int main(){
    std::cout<<"Your name: ";
    std::string name;
    std::cin>>name;
    //std::int age;
    //std::cin>>age;
    
    const std::string greeting = "* Hello, "+name+"! *";
    const std::string spaces(greeting.size()-2, ' ');
    const std::string second="*"+spaces+"*";
    const std::string first(greeting.size(),'*');

    std::cout<<first<<std::endl;
    std::cout<<second<<std::endl;
    std::cout<<greeting<<std::endl;
    std::cout<<second<<std::endl;
    std::cout<<first<<std::endl;


    const std::string hello="Hello";
    const std::string message = hello+", world"+"!";
    std::cout<<message<<std::endl;

    {
        const std::string s = "a string";
        std::cout<<s<<std::endl;
        {
            const std::string s= "another";
            std::cout<<s<<std::endl;
        }
    }
    std::cout<<"What is your name?";
    //std::string name;
    std::cin>>name;
    std::cout<<"Hello, "<<name<< "\n"<< "And what is yours?"; // 2개 이상을 같이 출력하려면 << 계속 써줘야 한다, endl이 \n으로 대체 가능한 듯.

    return 0;
}