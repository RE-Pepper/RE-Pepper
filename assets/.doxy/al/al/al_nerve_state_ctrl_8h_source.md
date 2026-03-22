

# File alNerveStateCtrl.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Nerve**](dir_cea16a3cd0068aab539e5f3441822a40.md) **>** [**alNerveStateCtrl.h**](al_nerve_state_ctrl_8h.md)

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


