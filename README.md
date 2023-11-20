# Auto-generate-header
Auto-generate C++ header file from class

Usage:
Provide the main Python script with the path to a CPP file containing a class. 
This will automatically generate a header file and a CPP file containing the methods.

Example usage (Linux):
python3 main.py example.cpp

For instance, the file example.cpp could contain a class structured like this:

```
#include <iostream>
#include <vector>

class Port {
    private:
        std::vector<int> boatIds;
        int freeSlots = 100;
        double money = 0.;
    public:
        void parkBoat(int id) {
            this->boatIds.push_back(id);
            this->freeSlots -= 1;
            this->money += 10.;
        }
        void removeBoat(int id) {
            for (int i = 0; i < this->boatIds.size(); i++) {
                if (id == this->boatIds[i]) {
                    this->boatIds.erase(this->boatIds.begin() + i);
                }
            }
            this->freeSlots += 1;
        }
        
        double getMoney() {
            return this->money;
        }
        
        int getFreeSlots() {
            return this->freeSlots;
        }
    
};
```

The Python script will then generate two files: Port.cpp and Port.h, which would look like this:

```
// Port.cpp

#include "Port.h"

void Port::parkBoat(int id) {
    this->boatIds.push_back(id);
    this->freeSlots -= 1;
    this->money += 10.;
}

void Port::removeBoat(int id) {
    for (int i = 0; i < this->boatIds.size(); i++) {
        if (id == this->boatIds[i]) {
            this->boatIds.erase(this->boatIds.begin() + i);
        }
    }
    this->freeSlots += 1;
}

double Port::getMoney() {
    return this->money;
}

int Port::getFreeSlots() {
    return this->freeSlots;
}
```

```
// Port.h

#ifndef PORT_H
#define PORT_H

#include <iostream>
#include <vector>

class Port {
    private:
        std::vector<int> boatIds;
        int freeSlots = 100;
        double money = 0.;
    public:
        void parkBoat(int id);
        void removeBoat(int id);
        double getMoney();
        int getFreeSlots();
};

#endif
```

Now you can conveniently include the Port.h header file in your project. 
Don't forget to add the generated CPP file to your build command.
