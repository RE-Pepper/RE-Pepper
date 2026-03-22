

# File SaveDataAccessSequence.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**System**](dir_e1006d71d276319c0715d176f1f44d04.md) **>** [**SaveDataAccessSequence.h**](_save_data_access_sequence_8h.md)

[Go to the documentation of this file](_save_data_access_sequence_8h.md)


```C++
#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{
class LayoutInitInfo;
}
class GameDataHolder;

class SaveDataAccessSequence : public al::NerveExecutor
{
private:
        // ...
public:
        SaveDataAccessSequence( GameDataHolder* holder, const al::LayoutInitInfo& info );
};
```


