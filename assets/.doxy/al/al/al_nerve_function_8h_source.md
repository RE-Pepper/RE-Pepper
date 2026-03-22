

# File alNerveFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Nerve**](dir_cea16a3cd0068aab539e5f3441822a40.md) **>** [**alNerveFunction.h**](al_nerve_function_8h.md)

[Go to the documentation of this file](al_nerve_function_8h.md)


```C++
#pragma once

#include <Nerve/alNerveKeeper.h>
#include <Nerve/alNerveStateBase.h>

namespace al
{
class NerveStateBase;

void setNerve( IUseNerve* p, const Nerve* nerve );

bool isStep( IUseNerve* p, int step );
bool isNerve( const IUseNerve* p, const Nerve* nerve );
bool isFirstStep( const IUseNerve* p );
bool isLessStep( const IUseNerve* p, int step );
int  getNerveStep( const IUseNerve* p );
bool isGreaterStep( const IUseNerve* p, int step );
bool isGreaterEqualStep( const IUseNerve* p, int step );

void initNerveState( IUseNerve* p, NerveStateBase* state, const Nerve* stateNrv, const char* name );
bool updateNerveState( IUseNerve* p );                                 // returns if nerve state is dead
bool updateNerveStateAndNextNerve( IUseNerve* p, const Nerve* nerve ); // "

} // namespace al

namespace alNerveFunction
{

void setNerveAction( al::IUseNerve* p, const char* name );

} // namespace alNerveFunction
```


