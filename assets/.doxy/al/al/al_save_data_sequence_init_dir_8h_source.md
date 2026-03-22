

# File alSaveDataSequenceInitDir.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Save**](dir_33ac68c743ce979100635e8d517aca20.md) **>** [**alSaveDataSequenceInitDir.h**](al_save_data_sequence_init_dir_8h.md)

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


