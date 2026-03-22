

# File alNerveStateCtrl.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Nerve**](dir_8d6afa48c7513136f8b448a486977ca0.md) **>** [**alNerveStateCtrl.cpp**](al_nerve_state_ctrl_8cpp.md)

[Go to the documentation of this file](al_nerve_state_ctrl_8cpp.md)


```C++
#include <Nerve/alNerveStateBase.h>
#include <Nerve/alNerveStateCtrl.h>

namespace al
{

NerveStateCtrl::NerveStateCtrl( int capacity )
    : mCapacity( capacity ), mStateCount( 0 ), mStates( nullptr ), mCurrentState( nullptr )
{
        mStates = new State[ mCapacity ];
        for ( int i = 0; i < mCapacity; i++ )
        {
                State* state           = &mStates[ i ];
                state->mState          = nullptr;
                state->mHostStateNerve = nullptr;
                state->mName           = nullptr;
        }
}

NerveStateCtrl::State* NerveStateCtrl::findStateInfo( const Nerve* nerve )
{
        for ( int i = 0; i < mStateCount; i++ )
        {
                State* state = &mStates[ i ];

                if ( state->mHostStateNerve == nerve )
                        return state;
        }

        return nullptr;
}

void NerveStateCtrl::startState( const Nerve* nerve )
{
        mCurrentState = findStateInfo( nerve );

        if ( mCurrentState )
                mCurrentState->mState->appear();
}

bool NerveStateCtrl::updateCurrentState()
{
        if ( mCurrentState )
                return mCurrentState->mState->update();
        return false;
}

void NerveStateCtrl::tryEndCurrentState()
{
        if ( !isCurrentStateEnd() )
        {
                mCurrentState->mState->kill();
                mCurrentState = nullptr;
        }
}

bool NerveStateCtrl::isCurrentStateEnd() const
{
        if ( mCurrentState )
                return mCurrentState->mState->isDead();
        return true;
}

} // namespace al
```


