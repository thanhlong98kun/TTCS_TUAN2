#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <fstream>
using namespace std;

#define nameWidth 20
#define numWidth 8
#define separator ' '
class Emp {
private:
	int id;
	string name;
	int age;
	int salaryBasic;
public:
	// GET
	int getId();
	string getName();
	int getSalaryBasic();
	int getAge();
	// SET
	void setId(int Id);
	void setName(string Name);
	void setSalaryBasic(int Salary);
	void setAge(int Age);
	Emp(int Id, string Name, int Age, int SalaryBasic);
};

// GET
int Emp::getId()
{
	return id;
}

string Emp::getName()
{
	return name;
}

int Emp::getSalaryBasic()
{
	return salaryBasic;
}

int Emp::getAge()
{
	return age;
}
// SET
void Emp::setId(int Id) {
	this->id = Id;
}

void Emp::setName(string Name)
{
	this->name = Name;
}

void Emp::setSalaryBasic(int Salary)
{
	this->salaryBasic = Salary;
}

void Emp::setAge(int Age)
{
	this->age = Age;
}

Emp::Emp(int Id, string Name, int Age, int SalaryBasic)
{
	this->id = Id;
	this->name = Name;
	this->age = Age;
	this->salaryBasic = SalaryBasic;
}

class DSNV {
private:
	vector<Emp*> list;
	int size = 0;
public:
	int getSize();
	int indexEmpById(int id);

	void readFromFile(string path);
	void writeFile(string path);
	void addEmp();
	void delEmp(int index);
	void editEmp(int index);
	void showAllEmp();
	void showOneEmp(int index);
};

int DSNV::getSize() {
	return size;
}

// Lay chi so cua nhan vien co ma nhan vien la: id
int DSNV::indexEmpById(int id) {
	for (int i = 0; i < this->size; i++) {
		if (this->list.at(i)->getId() == id) {
			return i;
		}
	}
	return -1;
}

void DSNV::readFromFile(string path)
{
	int id, age, salary;
	string name = "";
	string temp;
	ifstream file;
	file.open(path.c_str());
	if (file.fail()) {
		cout << "KHONG THE MO FILE" << endl;
		return;
	}
	while (!file.eof())
	{
		file >> id;
		file.ignore();
		getline(file, name);
		file >> age;
		file >> salary;
		this->list.push_back(new Emp(id, name, age, salary));
		this->size += 1	;
	}
	file.close();
}

void DSNV::writeFile(string path) {
	ofstream file;
	file.open(path.c_str(), ios::out|ios::binary);
	if (file.is_open()) {
		for (int i = 0; i < size; i++) {
			file << list.at(i)->getId() << endl;
			file << list.at(i)->getName() << endl;
			file << list.at(i)->getAge() << endl;
			file << list.at(i)->getSalaryBasic() << endl;
		}
	}
	else {
		cout << "KHONG THE MO FILE" << endl;
	}
	file.close();
}

void DSNV::addEmp() {
	int id, age, salary;
	string name;
	cout << "NHAN VIEN THU : " << size + 1 << endl;
	cout << "Ma nhan vien: ";
	do {
		cin >> id;
		if (indexEmpById(id) != -1) {
			cout << "Da co ma nhan vien nay. Nhap lai: ";
		}
	} while (indexEmpById(id) != -1);
	cin.ignore();
	cout << "Ten: "; getline(cin, name);
	cout << "Tuoi: "; cin >> age;
	cout << "Luong co ban: "; cin >> salary;
	cout << endl;
	this->list.push_back(new Emp(id, name, age, salary));
	this->size += 1;
}

void DSNV::delEmp(int id) {
	if (indexEmpById(id) == -1) {
		cout << "KHONG CO NHAN VIEN CO MA LA " << id << endl;
		return;
	}
	this->list.erase(this->list.begin() + indexEmpById(id));
	this->size -= 1;
	cout << "XOA NHAN VIEN THANH CONG" << endl;
}


void menuEditEmp() {
	cout << "Sua gi:" << endl;
	cout << "1. Ma nhan vien" << endl;
	cout << "2. Ten nhan vien" << endl;
	cout << "3. Tuoi nhan vien" << endl;
	cout << "4. Luong co ban nhan vien" << endl;
}
void DSNV::editEmp(int index)
{
	int id, age, salary, temp;
	string name;
	if (indexEmpById(index) == -1) {
		cout << "KHONG CO NHAN VIEN NAY!" << endl;
	}
	else {
		menuEditEmp();
		cout << "Ban chon: "; cin >> temp;
		switch (temp)
		{
		case 1:
			cout << "Nhap ma nhan vien muon sua: ";
			do {
				cin >> id;
				if (indexEmpById(id) != -1) {
					cout << "Da co ma nhan vien nay. Nhap lai: ";
				}
			} while (indexEmpById(id) != -1);
			this->list.at(indexEmpById(index))->setId(id);
			break;
		case 2:
			cin.ignore();
			cout << "Nhap ten nhan vien muon sua: "; getline(cin, name);
			this->list.at(indexEmpById(index))->setName(name);
			break;
		case 3:
			cout << "Nhap tuoi nhan vien muon sua: "; cin >> age;
			this->list.at(indexEmpById(index))->setAge(age);
			break;
		case 4:
			cout << "Nhap luong co ban muon sua: "; cin >> salary;
			this->list.at(indexEmpById(index))->setSalaryBasic(salary);
			break;
		default:
			cout << "Nhap sai" << endl;
			break;
		}
		system("cls");
		cout << "SUA NHAN VIEN THANH CONG" << endl;
	}
}


void DSNV::showAllEmp() {
	cout << "DANH SACH TAT CA CAC NHAN VIEN:" << endl;
	cout << left << setw(nameWidth) << setfill(separator) << "Ma";
	cout << left << setw(nameWidth) << setfill(separator) << "Ho ten";
	cout << left << setw(nameWidth) << setfill(separator) << "Tuoi";
	cout << left << setw(nameWidth) << setfill(separator) << "Luong co ban";
	cout << endl;
	for (int i = 0; i < this->size; i++) {
		cout << left << setw(nameWidth) << setfill(separator) << this->list.at(i)->getId();
		cout << left << setw(nameWidth) << setfill(separator) << this->list.at(i)->getName();
		cout << left << setw(nameWidth) << setfill(separator) << this->list.at(i)->getAge();
		cout << left << setw(nameWidth) << setfill(separator) << this->list.at(i)->getSalaryBasic();
		cout << endl;
	}
	cout << endl;
}

void DSNV::showOneEmp(int id)
{
	if (indexEmpById(id) == -1) {
		cout << "KHONG CO NHAN VIEN CO MA " << id << endl;
		return;
	}
	int index = indexEmpById(id);
	cout << left << setw(nameWidth) << setfill(separator) << "Ma";
	cout << left << setw(nameWidth) << setfill(separator) << "Ho ten";
	cout << left << setw(nameWidth) << setfill(separator) << "Tuoi";
	cout << left << setw(nameWidth) << setfill(separator) << "Luong co ban";
	cout << endl;
	cout << left << setw(nameWidth) << setfill(separator) << this->list.at(index)->getId();
	cout << left << setw(nameWidth) << setfill(separator) << this->list.at(index)->getName();
	cout << left << setw(nameWidth) << setfill(separator) << this->list.at(index)->getAge();
	cout << left << setw(nameWidth) << setfill(separator) << this->list.at(index)->getSalaryBasic();
	cout << endl;
}

void menu() {
	cout << "=================MENU=================" << endl;
	cout << "0. Nhap nhan vien tu file" << endl;
	cout << "1. Them nhan vien" << endl;
	cout << "2. Danh sach tat ca nhan vien" << endl;
	cout << "3. Sua nhan vien theo id" << endl;
	cout << "4. Xoa nhan vien theo id" << endl;
	cout << "5. Thong tin nhan vien theo id" << endl;
	cout << "6. Thoat" << endl;
}

void select(DSNV &list) {
	int n = 0, temp;
	menu();
	cout << "Ban chon: ";

	do {
		cin >> n;
		if ((n != 0 && n != 1 && n!= 6) && (list.getSize() == 0)) {
			cout << "Nhap lai: ";
		}
	} while ((n != 0 && n != 1 && n != 6) && (list.getSize() == 0));
	if (n == 6 && list.getSize() == 0) {
		return;
	}
	if (n == 6 && list.getSize() > 0) {
		list.writeFile("output3.dat");
		return;
	}
	switch (n)
	{
	case 0:
		list.readFromFile("input2.txt");
		system("cls");
		cout << "NHAP NHAN VIEN TU FILE THANH CONG" << endl;
		select(list);
		break;
	case 1:
		list.addEmp();
		system("cls");
		cout << "THEM NHAN VIEN THANH CONG" << endl;
		select(list);
		break;
	case 2:
		system("cls");
		list.showAllEmp();
		select(list);
		break;
	case 3:
		cout << "Nhap ma nhan vien muon sua:"; cin >> temp;
		system("cls");
		list.editEmp(temp);
		select(list);
		break;
	case 4:
		cout << "Nhap ma nhan vien muon xoa:"; cin >> temp;
		system("cls");
		list.delEmp(temp);
		select(list);
		break;
	case 5:
		cout << "Nhap ma nhan vien muon xem:"; cin >> temp;
		system("cls");
		list.showOneEmp(temp);
		select(list);
		break;
	default:
		system("cls");
		cout << "Nhap sai" << endl;
		select(list);
		break;
	}
}


int main() {
	DSNV list;
	select(list);
	system("pause");
}
