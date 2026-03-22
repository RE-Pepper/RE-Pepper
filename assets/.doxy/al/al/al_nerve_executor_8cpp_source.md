

# File alNerveExecutor.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Nerve**](dir_8d6afa48c7513136f8b448a486977ca0.md) **>** [**alNerveExecutor.cpp**](al_nerve_executor_8cpp.md)

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


