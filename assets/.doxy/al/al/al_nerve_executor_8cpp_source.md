

# File alNerveExecutor.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Nerve**](dir_32e08f09dddceca537f9274884ee9aa2.md) **>** [**alNerveExecutor.cpp**](al_nerve_executor_8cpp.md)

[Go to the documentation of this file](al_nerve_executor_8cpp.md)


```C++
#include <Nerve/alNerveExecutor.h>

namespace al
{

NerveExecutor::NerveExecutor( const char* name ) : mNerveKeeper( nullptr )
{
}

NerveKeeper* NerveExecutor::getNerveKeeper() const
{
        return mNerveKeeper;
}

void NerveExecutor::initNerve( const Nerve* nrv, int step )
{
        mNerveKeeper = new NerveKeeper( this, nrv, step );
}

void NerveExecutor::updateNerve()
{
        if ( mNerveKeeper )
                mNerveKeeper->update();
}

} // namespace al
```


