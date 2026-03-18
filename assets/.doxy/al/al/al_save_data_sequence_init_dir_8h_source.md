

# File alSaveDataSequenceInitDir.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Save**](dir_fec35835b019f224ced7f4d2afb3cf47.md) **>** [**alSaveDataSequenceInitDir.h**](al_save_data_sequence_init_dir_8h.md)

[Go to the documentation of this file](al_save_data_sequence_init_dir_8h.md)


```C++
#pragma once

#include <Save/alSaveDataSequenceBase.h>

namespace al
{

class SaveDataSequenceInitDir : public SaveDataSequenceBase
{
public:
        SaveDataSequenceInitDir();

        virtual void threadFunc( const char* );
};

} // namespace al
```


