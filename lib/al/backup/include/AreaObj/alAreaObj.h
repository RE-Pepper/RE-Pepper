#pragma once

#include <Stage/alStageSwitchKeeper.h>
#include <math/seadMatrix.h>
#include <math/seadVector.h>

namespace al
{
class AreaInitInfo;
class AreaShape;
class StageSwitchKeeper;

class AreaObj : public IUseStageSwitch
{
private:
        const char*        mName;
        AreaShape*         mAreaShape;
        StageSwitchKeeper* mStageSwitchKeeper;
        sead::Matrix34f    _10;
        void*              _40;
        int                _44;
        bool               _48;

public:
        virtual StageSwitchKeeper* getStageSwitchKeeper() const;
        virtual void               initStageSwitchKeeper();
        virtual void               init( const AreaInitInfo& info );
        virtual bool               isInVolume( const sead::Vector3f& trans ) const;

public:
        AreaObj( const char* name );
};

} // namespace al
