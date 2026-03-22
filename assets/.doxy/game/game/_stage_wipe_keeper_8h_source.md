

# File StageWipeKeeper.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Sequence**](dir_add35431d27bbd5f0559725cdc453615.md) **>** [**StageWipeKeeper.h**](_stage_wipe_keeper_8h.md)

[Go to the documentation of this file](_stage_wipe_keeper_8h.md)


```C++
#pragma once

namespace al
{
class LayoutInitInfo;
class WipeSimpleTopBottom;
} // namespace al

class StageWipeKeeper
{
private:
        al::WipeSimpleTopBottom* mWipes[ 7 ];
        void*                    unk;

public:
        bool isAnyWipeCloseEnd() const;

public:
        StageWipeKeeper( const al::LayoutInitInfo& info );
};
```


