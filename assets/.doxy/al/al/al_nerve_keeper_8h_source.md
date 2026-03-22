

# File alNerveKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Nerve**](dir_cea16a3cd0068aab539e5f3441822a40.md) **>** [**alNerveKeeper.h**](al_nerve_keeper_8h.md)

[Go to the documentation of this file](al_nerve_keeper_8h.md)


```C++
#pragma once

namespace al
{

struct Nerve;
class IUseNerve;
class NerveStateCtrl;
class NerveActionCtrl;

class NerveKeeper
{
private:
        IUseNerve*       mHost;
        const Nerve*     mEndNerve;
        const Nerve*     mNerve;
        int              mStep;
        NerveStateCtrl*  mStateCtrl;
        NerveActionCtrl* mActionCtrl;

public:
        const Nerve* getCurrentNerve() const;

        void initNerveAction( NerveActionCtrl* p )
        {
                mActionCtrl = p;
        }

        void update();
        void tryChangeNerve();
        void setNerve( const Nerve* nerve );

        IUseNerve* getHost()
        {
                return mHost;
        }

        int getStep()
        {
                return mStep;
        }

        NerveStateCtrl* getStateCtrl()
        {
                return mStateCtrl;
        }

        NerveActionCtrl* getActionCtrl()
        {
                return mActionCtrl;
        }

public:
        NerveKeeper( IUseNerve* host, const Nerve* nrv, int maxNerveStates = 0 );
};

class IUseNerve
{
public:
        virtual NerveKeeper* getNerveKeeper() const = 0;
};

static_assert( sizeof( NerveKeeper ) == 0x18, "" );

} // namespace al
```


