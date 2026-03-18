

# File alNerveStateCtrl.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Nerve**](dir_32e08f09dddceca537f9274884ee9aa2.md) **>** [**alNerveStateCtrl.cpp**](al_nerve_state_ctrl_8cpp.md)

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


