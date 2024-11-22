#include <stdafx.h>
#include <sapi.h>
//#include <iostream>
//#include <string>

int main(int argc, const char* argv[])
{
    ISpVoice* pVoice = NULL;

    if (FAILED(::CoInitialize(NULL)))
        //std::cout << "Error!";
        return 1;

    HRESULT hr = CoCreateInstance(CLSID_SpVoice, NULL, CLSCTX_ALL, IID_ISpVoice, (void**)&pVoice);
    if (SUCCEEDED(hr))
    {
        if (argc == 2) {
            //std::wcout<< (const WCHAR*)argv[1];
            const char* pszMultiByte = argv[1] ;  //strlen(pwsUnicode)=5
            int iSize;
            wchar_t* pwszUnicode;

            //返回接受字符串所需缓冲区的大小，已经包含字符结尾符'\0'
            iSize = MultiByteToWideChar(CP_ACP, 0, pszMultiByte, -1, NULL, 0); //iSize =wcslen(pwsUnicode)+1=6
            pwszUnicode = (wchar_t*)malloc(iSize * sizeof(wchar_t)); //不需要 pwszUnicode = (wchar_t *)malloc((iSize+1)*sizeof(wchar_t))
            MultiByteToWideChar(CP_ACP, 0, pszMultiByte, -1, (LPWSTR)pwszUnicode , iSize);

            hr = pVoice->Speak(pwszUnicode, SPF_IS_XML, NULL);
            //hr = pVoice->Speak(L"I am running", SPF_IS_XML, NULL);
        }
        else {
            hr = pVoice->Speak(L" <volume level='100'>Error: The number of parameters is not enough.错误:参数不足", SPF_IS_XML, NULL);
        }
        pVoice->Release();
        pVoice = NULL;
    }
    ::CoUninitialize();
    return 0;
}