

# Class nn::Result



[**ClassList**](annotated.md) **>** [**nn**](namespacenn.md) **>** [**Result**](classnn_1_1_result.md)





* `#include <Result.h>`

















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**Description**](#enum-description)  <br> |
| enum  | [**Level**](#enum-level)  <br> |
| enum  | [**ModuleType**](#enum-moduletype)  <br> |
| enum  | [**Summary**](#enum-summary)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  bool | [**Failed**](#function-failed) () const<br> |
|  int | [**GetDescription**](#function-getdescription) () const<br> |
|  [**Level**](classnn_1_1_result.md#enum-level) | [**GetLevel**](#function-getlevel) () const<br> |
|  [**ModuleType**](classnn_1_1_result.md#enum-moduletype) | [**GetModuleType**](#function-getmoduletype) () const<br> |
|  [**Summary**](classnn_1_1_result.md#enum-summary) | [**GetSummary**](#function-getsummary) () const<br> |
|  bool | [**IsValid**](#function-isvalid) () const<br> |
|   | [**Result**](#function-result-12) () <br> |
|   | [**Result**](#function-result-22) ([**Level**](classnn_1_1_result.md#enum-level) level, [**Summary**](classnn_1_1_result.md#enum-summary) summary, [**ModuleType**](classnn_1_1_result.md#enum-moduletype) module, int desc) <br> |
|  bool | [**Succeeded**](#function-succeeded) () const<br> |
|   | [**operator bool**](#function-operator-bool) () <br> |




























## Public Types Documentation




### enum Description 

```C++
enum nn::Result::Description {
    Description_InvalidSelection = 1000,
    Description_TooLarge,
    Description_NotAuthorized,
    Description_AlreadyDone,
    Description_InvalidSize,
    Description_InvalidEnumValue,
    Description_InvalidCombination,
    Description_NoData,
    Description_Busy,
    Description_MisalignedAddress,
    Description_MisalignedSize,
    Description_OutOfMemory,
    Description_NotImplemented,
    Description_InvalidAddress,
    Description_InvalidPointer,
    Description_InvalidHandle,
    Description_NotInitialized,
    Description_AlreadyInitialized,
    Description_NotFound,
    Description_CancelRequested,
    Description_AlreadyExists,
    Description_OutOfRange,
    Description_Timeout,
    Description_InvalidResultValue,
    Description_Success = 0
};
```




<hr>



### enum Level 

```C++
enum nn::Result::Level {
    Level_Status = -7,
    Level_Temporary,
    Level_Permanent,
    Level_Usage,
    Level_Reinitialize,
    Level_Reset,
    Level_Fatal,
    Level_Info,
    Level_Success
};
```




<hr>



### enum ModuleType 

```C++
enum nn::Result::ModuleType {
    ModuleType_COMMON = 0,
    ModuleType_KERNEL = 1,
    ModuleType_UTIL = 2,
    ModuleType_FILE_SERVER = 3,
    ModuleType_LOADER_SERVER = 4,
    ModuleType_TCB = 5,
    ModuleType_OS = 6,
    ModuleType_DBG = 7,
    ModuleType_DMNT = 8,
    ModuleType_PDN = 9,
    ModuleType_GSP = 10,
    ModuleType_I2C = 11,
    ModuleType_GPIO = 12,
    ModuleType_DD = 13,
    ModuleType_CODEC = 14,
    ModuleType_SPI = 15,
    ModuleType_PXI = 16,
    ModuleType_FS = 17,
    ModuleType_DI = 18,
    ModuleType_HID = 19,
    ModuleType_CAM = 20,
    ModuleType_PI = 21,
    ModuleType_PM = 22,
    ModuleType_PM_LOW = 23,
    ModuleType_FSI = 24,
    ModuleType_SRV = 25,
    ModuleType_NDM = 26,
    ModuleType_NWM = 27,
    ModuleType_SOC = 28,
    ModuleType_LDR = 29,
    ModuleType_ACC = 30,
    ModuleType_ROMFS = 31,
    ModuleType_AM = 32,
    ModuleType_HIO = 33,
    ModuleType_UPDATER = 34,
    ModuleType_MIC = 35,
    ModuleType_FND = 36,
    ModuleType_MP = 37,
    ModuleType_MPWL = 38,
    ModuleType_AC = 39,
    ModuleType_HTTP = 40,
    ModuleType_DSP = 41,
    ModuleType_SND = 42,
    ModuleType_DLP = 43,
    ModuleType_HIO_LOW = 44,
    ModuleType_CSND = 45,
    ModuleType_SSL = 46,
    ModuleType_AM_LOW = 47,
    ModuleType_NEX = 48,
    ModuleType_FRIENDS = 49,
    ModuleType_RDT = 50,
    ModuleType_APPLET = 51,
    ModuleType_NIM = 52,
    ModuleType_PTM = 53,
    ModuleType_MIDI = 54,
    ModuleType_MC = 55,
    ModuleType_SWC = 56,
    ModuleType_FATFS = 57,
    ModuleType_NGC = 58,
    ModuleType_CARD = 59,
    ModuleType_CARDNOR = 60,
    ModuleType_SDMC = 61,
    ModuleType_BOSS = 62,
    ModuleType_DBM = 63,
    ModuleType_CONFIG = 64,
    ModuleType_PS = 65,
    ModuleType_CEC = 66,
    ModuleType_IR = 67,
    ModuleType_UDS = 68,
    ModuleType_PL = 69,
    ModuleType_CUP = 70,
    ModuleType_GYROSCOPE = 71,
    ModuleType_MCU = 72,
    ModuleType_NS = 73,
    ModuleType_NEWS = 74,
    ModuleType_RO = 75,
    ModuleType_GD = 76,
    ModuleType_CARD_SPI = 77,
    ModuleType_EC = 78,
    ModuleType_WEB_BROWSER = 79,
    ModuleType_TEST = 80,
    ModuleType_ENC = 81,
    ModuleType_PIA = 82,
    ModuleType_ACT = 83,
    ModuleType_VCTL = 84,
    ModuleType_OLV = 85,
    ModuleType_NEIA = 86,
    ModuleType_NPNS = 87,
    ModuleType_AVD = 90,
    ModuleType_L2B = 91,
    ModuleType_MVD = 92,
    ModuleType_NFC = 93,
    ModuleType_UART = 94,
    ModuleType_SPM = 95,
    ModuleType_QTM = 96,
    ModuleType_NFP = 97,
    ModuleType_APP = 254
};
```




<hr>



### enum Summary 

```C++
enum nn::Result::Summary {
    Summary_Success = 0,
    Summary_Nop = 1,
    Summary_WouldBlock = 2,
    Summary_OutOfResources = 3,
    Summary_NotFound = 4,
    Summary_InvalidState = 5,
    Summary_NotSupported = 6,
    Summary_InvalidArgument = 7,
    Summary_WrongArgument = 8,
    Summary_Cancelled = 9,
    Summary_StatusChanged = 10,
    Summary_Internal = 11,
    Summary_InvalidResultValue = 63
};
```




<hr>
## Public Functions Documentation




### function Failed 

```C++
inline bool nn::Result::Failed () const
```




<hr>



### function GetDescription 

```C++
inline int nn::Result::GetDescription () const
```




<hr>



### function GetLevel 

```C++
inline Level nn::Result::GetLevel () const
```




<hr>



### function GetModuleType 

```C++
inline ModuleType nn::Result::GetModuleType () const
```




<hr>



### function GetSummary 

```C++
inline Summary nn::Result::GetSummary () const
```




<hr>



### function IsValid 

```C++
inline bool nn::Result::IsValid () const
```




<hr>



### function Result [1/2]

```C++
inline nn::Result::Result () 
```




<hr>



### function Result [2/2]

```C++
inline nn::Result::Result (
    Level level,
    Summary summary,
    ModuleType module,
    int desc
) 
```




<hr>



### function Succeeded 

```C++
inline bool nn::Result::Succeeded () const
```




<hr>



### function operator bool 

```C++
inline nn::Result::operator bool () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `lib/CtrSDK/include/nn/Result.h`

