# include<iostream>
# include<cstring>

// using namespace std;
using std::cout;
using std::strcpy;
using std::endl;

// 定义 Books_init
struct Books_init
{
	char  title[50];
	char  author[50];
	char  subject[100];
	int   book_id;
} book_i = {"标题", "作者", "C", 1111}, book_i2 = {"标题2", "作者2", "C2", 11112}, *book_i3;

struct Books
{
	char  title[50];
	char  author[50];
	char  subject[100];
	int   book_id;
};

void print_book(Books book_){
	cout<<book_.title<<endl;
	cout<<book_.author<<endl;
	cout<<book_.subject<<endl;
	cout<<book_.book_id<<endl;
}

void print_book_by_point(Books *book_){
	// cout<<book_->title<<endl;
	// cout<<book_->author<<endl;
	// cout<<book_->subject<<endl;
	// cout<<book_->book_id<<endl;
	printf("title : %s\nauthor: %s\nsubject: %s\nbook_id: %d\n",
		book_->title,
		book_->author,
		book_->subject,
		book_->book_id);
}

int main(){
	// 定义时赋值, 或者定义结构体的时候就赋值
	struct Books book1 = {"C Programming", "Nuha Ali", "C Programming Tutorial", 1001011};	// 参数顺序不能错

	// 定义好后赋值
	struct Books book2;
	strcpy(book2.title, "C Programming");
	strcpy(book2.author, "Nuha Ali");
	strcpy(book2.subject, "C Programming Tutorial");
	*book2.subject = ':';
	book2.book_id = 6495407;

	// C 风格乱序赋值
	struct Books book3 = {
		.title = "C Programming",
		.author = "Nuha Ali",
		.subject = "C Programming Tutorial",
		.book_id = 1001011,
		};

	// C++ 风格乱序赋值, 不过还是建议上面那个
	// struct Books book4 = {
	// 	title: "C Programming",
	// 	author: "Nuha Ali",
	// 	subject: "C Programming Tutorial",
	// 	book_id: 1001011,
	// 	};

	printf("======================1====================\n");
	print_book(book1);
	print_book(book2);
	print_book(book3);
	// print_book(book4);

	printf("======================2====================\n");
	print_book_by_point(&book1);
	print_book_by_point(&book2);
	print_book_by_point(&book3);
	// print_book_by_point(&book4);

	typedef int ad;
	ad b = 2;
	typedef int BOOL;
	BOOL TRUE = 1;
	BOOL FALSE = 0;
	typedef char A;
	A dd[10] = "hello";
	A const *ddd = "hello";
	char const *se = "hello";
	char const *see;
	see = "hello";
	printf("dd: %s,\nddd: %s\n", dd, ddd);

}


