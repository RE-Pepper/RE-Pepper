

# File alNerveKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Nerve**](dir_32e08f09dddceca537f9274884ee9aa2.md) **>** [**alNerveKeeper.cpp**](al_nerve_keeper_8cpp.md)

[Go to the documentation of this file](al_nerve_keeper_8cpp.md)


```C++
#include <Nerve/alNerve.h>
#include <Nerve/alNerveKeeper.h>
#include <Nerve/alNerveStateCtrl.h>

namespace al
{

NerveKeeper::NerveKeeper( IUseNerve* host, const Nerve* nrv, int maxNerveStates )
    : mEndNerve( nullptr ), mStep( 0 ), mStateCtrl( nullptr ), mActionCtrl( nullptr )
{
        mHost  = host;
        mNerve = nrv;

        if ( maxNerveStates > 0 )
                mStateCtrl = new NerveStateCtrl( maxNerveStates );
}

const Nerve* NerveKeeper::getCurrentNerve() const
{
        if ( mNerve )
                return mNerve;
        else
                return mEndNerve;
}

#ifdef NON_MATCHING
void NerveKeeper::update()
{
        tryChangeNerve();
        mNerve->execute( this );
        mStep++;
        tryChangeNerve();
}
#endif

void NerveKeeper::tryChangeNerve()
{
        if ( mNerve == NULL )
                return;

        if ( mStateCtrl )
        {
                mStateCtrl->tryEndCurrentState();
                mStateCtrl->startState( mNerve );
        }

        const Nerve* pNextState = mNerve;
        mStep                   = 0;
        mEndNerve               = pNextState;
        mNerve                  = NULL;
}

void NerveKeeper::setNerve( const Nerve* nerve )
{
        if ( mStep >= 0 && mEndNerve != nullptr )
                mEndNerve->executeOnEnd( this );
        mNerve = nerve;
        mStep  = -1;
}

} // namespace al
```


