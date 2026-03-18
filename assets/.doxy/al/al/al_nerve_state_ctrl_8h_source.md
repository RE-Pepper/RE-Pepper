

# File alNerveStateCtrl.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Nerve**](dir_0d638fa675477dde0733aed9f19ea6f2.md) **>** [**alNerveStateCtrl.h**](al_nerve_state_ctrl_8h.md)

[Go to the documentation of this file](al_nerve_state_ctrl_8h.md)


```C++
#pragma once

#include <Nerve/alNerve.h>

namespace al
{
class NerveStateBase;

class NerveStateCtrl
{
private:
        struct State
        {
                NerveStateBase* mState;
                const Nerve*    mHostStateNerve;
                const char*     mName;
        };

        int    mCapacity;
        int    mStateCount;
        State* mStates;
        State* mCurrentState;

        State* findStateInfo( const Nerve* nerve );

public:
        const State* getCurrentState() const
        {
                return mCurrentState;
        }

        void startState( const Nerve* nerve );
        void tryEndCurrentState();
        bool updateCurrentState();
        bool isCurrentStateEnd() const;

public:
        NerveStateCtrl( int capacity );
};

} // namespace al
```


