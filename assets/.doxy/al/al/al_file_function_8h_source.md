

# File alFileFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**File**](dir_434e756ae3930eedc6101a4f10d5330c.md) **>** [**alFileFunction.h**](al_file_function_8h.md)

[Go to the documentation of this file](al_file_function_8h.md)


```C++
#pragma once

#include <prim/seadSafeString.h>

namespace al
{

bool isExistArchive( const sead::SafeString& archive );
void loadArchive( const sead::SafeString& archive );

void makeLocalizedArchivePath( sead::BufferedSafeString* out, const sead::SafeString& archive );
void makeStageDataArchivePath( sead::BufferedSafeString* out, const char* stageName, int scenario, const char* type /* Design, Map, Sound */ );

} // namespace al
```


