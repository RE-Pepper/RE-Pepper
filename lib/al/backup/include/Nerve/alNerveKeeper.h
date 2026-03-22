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
