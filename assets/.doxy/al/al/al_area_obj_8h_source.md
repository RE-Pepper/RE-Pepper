

# File alAreaObj.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**AreaObj**](dir_65406aa8482a23b720984def0cee3032.md) **>** [**alAreaObj.h**](al_area_obj_8h.md)

[Go to the documentation of this file](al_area_obj_8h.md)


```C++
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
```


