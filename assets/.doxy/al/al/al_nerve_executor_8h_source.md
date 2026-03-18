

# File alNerveExecutor.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Nerve**](dir_0d638fa675477dde0733aed9f19ea6f2.md) **>** [**alNerveExecutor.h**](al_nerve_executor_8h.md)

[Go to the documentation of this file](al_nerve_executor_8h.md)


```C++
#pragma once

#include <Nerve/alNerveKeeper.h>

namespace al
{
class NerveKeeper;

class NerveExecutor : public IUseNerve
{
private:
        al::NerveKeeper* mNerveKeeper;

public:
        void initNerve( const Nerve*, int step = 0 );
        void updateNerve();

public:
        virtual NerveKeeper* getNerveKeeper() const;
        virtual ~NerveExecutor() {};

public:
        NerveExecutor( const char* name );
};

} // namespace al
```


