#include <bits/stdc++.h>

using namespace std;

double integrate(function<double(double)> f, double a, double b, double n) {
	double result = 0;

	double del_x = (b - a) / n;

	result += 0.5 * f(a);

	int i = 1;
	for (i = 1; i < n - 2; ++i) {
		result += f(a + i * del_x);
	}

	result += 0.5 * f(b - del_x);

	result *= del_x;

	return result;
}

int main() {
	cout << integrate([](const double x) { return pow(4 + x, x); }, 1, 4, 20)
		 << "\n";
}