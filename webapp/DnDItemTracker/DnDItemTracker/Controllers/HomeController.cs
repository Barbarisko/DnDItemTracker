using DnDItemTracker.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace DnDItemTracker.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            var character = new CharacterModel();
            character.slotsModel.title = "Spell Slots";
            character.slotsModel.spellSlots.Add(Tuple.Create("Level I", new List<bool> { true, true, false }));
            character.slotsModel.spellSlots.Add(Tuple.Create("Level II", new List<bool> { false, true, false }));

            character.specialPowerModel.title = "Special Powers";
            character.specialPowerModel.spellSlots.Add(Tuple.Create("Monk Tsy points", new List<bool> { true, true, false }));

            return View(character) ;
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
