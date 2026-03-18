

# File alFileFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**File**](dir_9b6dcd94aa4037af52ac57e311dd7dc6.md) **>** [**alFileFunction.cpp**](al_file_function_8cpp.md)

[Go to the documentation of this file](al_file_function_8cpp.md)


```C++
#include <File/alFileFunction.h>
#include <File/alFileLoader.h>
#include <Message/alMessageFunction.h>
#include <System/alSystemKit.h>
#include <Util/alStringUtil.h>

namespace al
{

void loadArchive( const sead::SafeString& archive )
{
        alProjectInterface::getSystemKit()->getFileLoader()->loadArchive(
                StringTmp<256>( "%s.szs", archive.cstr() ), nullptr );
}

void makeLocalizedArchivePath( sead::BufferedSafeString* out, const sead::SafeString& archive )
{
        out->format( "LocalizedData/%s/%s", al::getLanguage(), archive.cstr() );
}

void makeStageDataArchivePath( sead::BufferedSafeString* out, const char* stageName, int scenario, const char* type )
{
        out->format( "StageData/%s%s%d", stageName, type, scenario );
}

} // namespace al
```


