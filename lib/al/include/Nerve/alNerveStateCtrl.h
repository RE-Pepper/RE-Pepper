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
