#pragma checksum "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\Home\Index.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "9314f076898c909db269af93fae6f8309989948c"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Home_Index), @"mvc.1.0.view", @"/Views/Home/Index.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\_ViewImports.cshtml"
using DnDItemTracker;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\_ViewImports.cshtml"
using DnDItemTracker.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"9314f076898c909db269af93fae6f8309989948c", @"/Views/Home/Index.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"97c3fcf8fd9c56df17afd852ae4bb3dd739aea15", @"/Views/_ViewImports.cshtml")]
    public class Views_Home_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<CharacterModel>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 2 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\Home\Index.cshtml"
  
    ViewData["Title"] = "Home Page";

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n<div class=\"container mt-2 mb-4\">\r\n    <div class=\"row\">\r\n        <div class=\"pt-4 col-sm-12 col-md-6\">\r\n\r\n            ");
#nullable restore
#line 10 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\Home\Index.cshtml"
       Write(await Html.PartialAsync("_SpellTitle", Model.slotsModel));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            ");
#nullable restore
#line 11 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\Home\Index.cshtml"
       Write(await Html.PartialAsync("_SpellSlots", Model.slotsModel));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n        </div>\r\n        <div class=\"pt-4 col-sm-12 col-md-6\">\r\n            ");
#nullable restore
#line 14 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\Home\Index.cshtml"
       Write(await Html.PartialAsync("_SpellTitle", Model.specialPowerModel));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            ");
#nullable restore
#line 15 "C:\Users\helen\source\repos\DnDItemTracker\webapp\DnDItemTracker\DnDItemTracker\Views\Home\Index.cshtml"
       Write(await Html.PartialAsync("_SpellSlots", Model.specialPowerModel));

#line default
#line hidden
#nullable disable
            WriteLiteral(@"
        </div>

        <div class=""pt-4 col-sm-12 col-md-6"">
            <div class=""container fs-2 fw-semibold  border rounded bg-light-subtle"">
                Consumables
            </div>
            <ul class=""pt-2 list-group"">
                <li class=""list-group-item"">
                    <div class=""row d-flex align-items-center"">
                        <div class=""col-8 d-flex"">
                            <div class=""fs-5 fw-semibold"">
                                Super Item
                            </div>
                            <span class=""m-1 badge bg-secondary align-self-stretch"">x5</span>
                        </div>
                        <div class=""col-4 d-flex justify-content-end"">
                            <div class=""btn-group"" role=""group"" aria-label=""Basic example"">
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">+</button>
                                <button type=""button"" class=""btn btn");
            WriteLiteral(@"-primary btn-sm"" style=""width: 40px"">-</button>
                            </div>
                        </div>
                    </div>
                    <div class=""row mt-1 mb-1 d-flex align-items-center"">
                        <small class=""col ms-3"">
                            Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print,
                            graphic or web designs.
                        </small>
                    </div>
                </li>
                <li class=""list-group-item"">
                    <div class=""row d-flex align-items-center"">
                        <div class=""col-8 d-flex"">
                            <div class=""fs-5 fw-semibold"">
                                Super Item
                            </div>
                            <span class=""m-1 badge bg-secondary align-self-stretch"">x5</span>
                        </div>
                        <div class=""col-4 d-flex justify-content-end");
            WriteLiteral(@""">
                            <div class=""btn-group"" role=""group"" aria-label=""Basic example"">
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">+</button>
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">-</button>
                            </div>
                        </div>
                    </div>
                    <div class=""row mt-1 mb-1 d-flex align-items-center"">
                        <small class=""col ms-3"">
                            Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print,
                            graphic or web designs.
                        </small>
                    </div>
                </li>
                <li class=""list-group-item"">
                    <button type=""button"" class=""btn btn-success"" style=""width: 100%;"">
                        Add
                    </button>

                </l");
            WriteLiteral(@"i>
            </ul>
        </div>

        <div class=""pt-4 col-sm-12 col-md-6"">
            <div class=""container fs-2 fw-semibold border rounded bg-light-subtle"">
                Artifacts
            </div>
            <div class=""pt-2 list-group"">
                <div class=""list-group-item"">
                    <div class=""row"">
                        <div class=""col-8"">
                            <h5 class=""p-1"">Super Item </h5>
                        </div>
                        <div class=""col-4 d-flex justify-content-end"">
                            <button type=""button"" class=""btn btn-outline-danger btn-sm align-self-center"">
                                Reset All
                            </button>
                        </div>
                    </div>
                    <div class=""row m-1 d-flex align-items-center"">
                        <small class=""col"">
                            Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in l");
            WriteLiteral(@"aying out
                            print,
                            graphic or web designs.
                        </small>
                    </div>
                    <div class=""row ps-2 pb-2 form-check-inline"">
                        <input class=""ms-2 mt-2 form-check-input big-checkbox"" type=""checkbox"" id=""inlineCheckbox1""");
            BeginWriteAttribute("value", "\r\n                               value=\"", 4976, "\"", 5016, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 5135, "\"", 5175, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 5294, "\"", 5334, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 5453, "\"", 5493, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 5612, "\"", 5652, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 5771, "\"", 5811, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 5930, "\"", 5970, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 6089, "\"", 6129, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 6248, "\"", 6288, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 6407, "\"", 6447, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 6566, "\"", 6606, 0);
            EndWriteAttribute();
            WriteLiteral(@">
                    </div>
                </div>
                <div class=""list-group-item"">
                    <div class=""row"">
                        <div class=""col-8"">
                            <h5 class=""p-1"">Super Item </h5>
                        </div>
                        <div class=""col-4 d-flex justify-content-end"">
                            <button type=""button"" class=""btn btn-outline-danger btn-sm align-self-center"">
                                Reset All
                            </button>
                        </div>
                    </div>
                    <div class=""row m-1 d-flex align-items-center"">
                        <small class=""col"">
                            Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out
                            print,
                            graphic or web designs.
                        </small>
                    </div>
                    <div class=""row ps-2 pb-2 ");
            WriteLiteral("form-check-inline\">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 7767, "\"", 7807, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 7926, "\"", 7966, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 8085, "\"", 8125, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 8244, "\"", 8284, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 8403, "\"", 8443, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 8562, "\"", 8602, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 8721, "\"", 8761, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 8880, "\"", 8920, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 9039, "\"", 9079, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 9198, "\"", 9238, 0);
            EndWriteAttribute();
            WriteLiteral(">\r\n                        <input class=\"ms-2 mt-2 form-check-input big-checkbox\" type=\"checkbox\" id=\"inlineCheckbox1\"");
            BeginWriteAttribute("value", "\r\n                               value=\"", 9357, "\"", 9397, 0);
            EndWriteAttribute();
            WriteLiteral(@">
                    </div>
                </div>
                <li class=""list-group-item"">
                    <button type=""button"" class=""btn btn-success"" style=""width: 100%;"">
                        Add
                    </button>

                </li>

            </div>
        </div>
        <div class=""pt-4 col-sm-12 col-md-6"">
            <div class=""container  fs-2 fw-semibold border rounded bg-light-subtle"">
                Light
            </div>
            <ul class=""pt-2 list-group"">
                <li class=""list-group-item"">
                    <input class=""form-check-input me-1"" type=""radio"" name=""listGroupRadio""");
            BeginWriteAttribute("value", " value=\"", 10066, "\"", 10074, 0);
            EndWriteAttribute();
            WriteLiteral(@" id=""firstRadio""
                           checked>
                    <label class=""form-check-label"" for=""firstRadio"">First radio</label>
                </li>
                <li class=""list-group-item"">
                    <input class=""form-check-input me-1"" type=""radio"" name=""listGroupRadio""");
            BeginWriteAttribute("value", " value=\"", 10380, "\"", 10388, 0);
            EndWriteAttribute();
            WriteLiteral(@"
                           id=""secondRadio"">
                    <label class=""form-check-label"" for=""secondRadio"">Second radio</label>
                </li>
                <li class=""list-group-item"">
                    <input class=""form-check-input me-1"" type=""radio"" name=""listGroupRadio""");
            BeginWriteAttribute("value", " value=\"", 10689, "\"", 10697, 0);
            EndWriteAttribute();
            WriteLiteral(@"
                           id=""thirdRadio"">
                    <label class=""form-check-label"" for=""thirdRadio"">Third radio</label>
                </li>
                <li class=""list-group-item"">
                    <button type=""button"" class=""btn btn-success"" style=""width: 100%;"">
                        Add
                    </button>

                </li>
            </ul>
        </div>

        <div class=""pt-4 col-sm-12 col-md-6"">
            <div class=""container fs-2 fw-semibold  border rounded bg-light-subtle"">
                Money
            </div>
            <ul class=""pt-2 list-group"">
                <li class=""list-group-item"">
                    TODO
                </li>
            </ul>
        </div>
        <div class=""pt-4 col-12"">
            <div class=""container fs-2 fw-semibold  border rounded bg-light-subtle"">
                Backpack
            </div>
            <ul class=""pt-2 list-group"">
                <li class=""list-group-item"">
    ");
            WriteLiteral(@"                <button type=""button"" class=""btn btn-success"" style=""width: 100%;"">
                        Add
                    </button>
                </li>
                <li class=""list-group-item"">
                    <div class=""row d-flex align-items-center"">
                        <div class=""col-8 d-flex"">
                            <div class=""fs-5 fw-semibold"">
                                Rope
                            </div>
                            <span class=""m-1 badge bg-secondary align-self-stretch"">x5</span>
                        </div>
                        <div class=""col-4 d-flex justify-content-end"">
                            <div class=""btn-group"" role=""group"" aria-label=""Basic example"">
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">+</button>
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">-</button>
                            </div");
            WriteLiteral(@">
                        </div>
                    </div>
                    <div class=""row m-2 d-flex align-items-center"">
                        <small class=""col"">
                            Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print,
                            graphic or web designs.
                        </small>
                    </div>

                    <div class=""row m-1 justify-content-end"">
                        <div class=""col-lg-4 col-9 btn-group"" role=""group"" aria-label=""Basic mixed styles example"">
                            <button type=""button"" class=""btn btn-danger"">Delete</button>
                            <button type=""button"" class=""btn btn-primary"">Edit</button>
                            <button type=""button"" class=""btn btn-success"">Duplicate</button>
                        </div>
                    </div>
                </li>
                <li class=""list-group-item"">
                    <div class");
            WriteLiteral(@"=""row d-flex align-items-center"">
                        <div class=""col-8 d-flex"">
                            <div class=""fs-5 fw-semibold"">
                                Bottle
                            </div>
                            <span class=""m-1 badge bg-secondary align-self-stretch"">x5</span>
                        </div>
                        <div class=""col-4 d-flex justify-content-end"">
                            <div class=""btn-group"" role=""group"" aria-label=""Basic example"">
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">+</button>
                                <button type=""button"" class=""btn btn-primary btn-sm"" style=""width: 40px"">-</button>
                            </div>
                        </div>
                    </div>
                    <div class=""row m-2 d-flex align-items-center"">
                        <small class=""col"">
                            Lorem ipsum, or lipsum as it is somet");
            WriteLiteral(@"imes known, is dummy text used in laying out print,
                            graphic or web designs.
                        </small>
                    </div>

                    <div class=""row m-1 justify-content-end"">
                        <div class=""col-lg-4 col-9 btn-group"" role=""group"" aria-label=""Basic mixed styles example"">
                            <button type=""button"" class=""btn btn-danger"">Delete</button>
                            <button type=""button"" class=""btn btn-primary"">Edit</button>
                            <button type=""button"" class=""btn btn-success"">Duplicate</button>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>
");
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<CharacterModel> Html { get; private set; }
    }
}
#pragma warning restore 1591
